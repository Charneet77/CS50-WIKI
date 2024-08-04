import os
import markdown
import re

from django.shortcuts import render, redirect
from . import util
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from .models import MarkdownFile

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add(request):
    return render(request, "add.html")

def save(request):
    if request.method == 'POST':
        title = request.POST['title']
        print(title)
        content = request.POST['content']

        util.save_entry(title, content)

        print("Entry Saved")
        return redirect(f"{title}.md")
    else:
        return render(request,'add.html')

def render_markdown(request, filename):
    # Define the path to the markdown files
    md_dir = os.path.join(settings.BASE_DIR, 'entries')
    md_file = os.path.join(md_dir, f"{filename}.md")
    
    # Check if the file exists
    if not os.path.exists(md_file):
        raise Http404("Markdown file not found")

    # Read the markdown file
    with open(md_file, 'r') as file:
        md_content = file.read()

    # Convert markdown content to HTML
    html_content = markdown.markdown(md_content)

    # Extract the title from the markdown content
    title_line = md_content.split('\n', 1)[0]
    if title_line.startswith('# '):
        title = title_line[2:]
    else:
        title = "Untitled Document"

    return render(request, 'TITLE.html', {'content': html_content, 'title': title})

def search_markdown(request):
    if request.method == "POST":
        query = request.POST.get('q')
        entries_dir = os.path.join(settings.BASE_DIR, 'entries')
        results = []

        # Search for files containing the query
        for filename in os.listdir(entries_dir):
            if filename.endswith('.md'):
                filepath = os.path.join(entries_dir, filename)
                with open(filepath, 'r') as file:
                    content = file.read()
                    if re.search(query, content, re.IGNORECASE):
                        results.append({
                            'title': filename[:-3],  # remove .md extension
                            'content': markdown.markdown(content)
                        })
        
        return render(request, 'search.html', {'results': results, 'query': query})

    return redirect('index')  # Redirect to an appropriate page if the request is not POST