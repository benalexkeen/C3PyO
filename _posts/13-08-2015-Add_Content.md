---
layout: post
title: Add Content
category: docs
excerpt: Adding documentation
---

## Add project
{: .content-subhead }

Follow the instructions to add a new project:

* Go to `_data > categories.yml`. Remove the default `docs` and add your project instead.
* If you're having single project, you probably would like to use something generic like `documentation` or `docs`.
* If you're maving multiple projects, you can use project name.

Now you need to create a project page. To do that:

* Go to `projects` folder and add a new file with the project slug as file name. You can use .md as extension if you're using Markdown, .textile if you're using Textile, or .html if you want to write raw html. 
* Add the metadata into that file. Copy the meta information from header of default `docs.md` and modify the information.  
**layout**: project  
**title**: Project Name  
**category**: Project Slug as in `categories.yml`.  
**permalink**: Project Slug with a forward slash.

## Add post
{: .content-subhead }

Now you're ready to write the documentation. Add a new file in `_posts` folder. File name structure must start with the date. The name after date would be used as slug.

Add metadata to the post. Copy the meta information from sample pages. Probably you know now what to do with it.

Read more about [writing posts on Jekyll documentation](http://jekyllrb.com/docs/posts/).

## Edit Homepage
{: .content-subhead }

I've written index.html in HTML so that you can customize it however you wish!
