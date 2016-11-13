---
layout: post
title: Structure
category: docs
excerpt: What are all these folders?
---

Algomash uses Jekyll and hence uses the defined directory structure.

## _data
{: .content-subhead }

This folder contains extra site data like categories and tags. The data can be accessed by `site.data` variable.

In Algomash, this folder contains a file called `categories.yml`. While adding content, you must add the name of your project and URL slug into this file. 

## _includes
{: .content-subhead }

If you've worked on a backend language like PHP, you know them! These ae separate parts of a webpage - common to all page usually - that we're including in our layouts like headers, footers.

## _layouts
{: .content-subhead }

Algomash uses 3 types of Jekyll layouts. If you've worked on some CMS like WordPress, then they're like Post Formats, where you can customize different post formats.

There are 3 post types in Algomash, Page, Post and Project. Algomash uses 
* Page for Index page
* Posts for the documentation
* Project for the first page of project's documentation.

If you want to create more pages, different from the index page layout, you can copy the `page.md` file in a separate file like `index.md`. Then open `index.html` in the root directory and change layout to `index`.

## _posts
{: .content-subhead }

These are the documentation pages for your project(s). The page you're currently reading is also saved there only.

## _site
{: .content-subhead }

While you won't get this folder in the package, you'll find it in the folder when you build the site using `jekyll build` or `jekyll serve`. This is the folder from where your website is served.

## assets
{: .content-subhead }

This folder contains CSS, JS and images.

## projects
{: .content-subhead }

The first page of your documentaion will be saved here. It does not need a date in front as posts but you should name it as the slug of your category or project.

This is a very basic oberview of these folders. I recommend you read [Jekyll documentation](http://jekyllrb.com/docs/structure/) to understand it better. It's very easy and powerful.