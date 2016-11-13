---
layout: post
title: Documentation
---

* Do not remove this line (it will not be displayed) 
{:toc}

# Installation
Fork the ``master`` branch and delete ``gh-pages`` branch in it. This is important because ``gh-pages`` branch is used here only to host the blog. You should be using the master branch as the source and create a fresh ``gh-pages`` branch.

## How to delete old ``gh-pages`` branch?
After forking the repository, click on **branches**.

![delete gh-pages branch]({{site.baseurl}}/images/delete-github-branch.png)

Delete ``gh-pages`` branch.
![delete gh-pages branch]({{site.baseurl}}/images/delete-github-branch-2.png)

You have to create a new ``gh-pages`` branch using the master branch. Go back to the forked repository and create ``gh-pages`` branch.

![create gh-pages branch]({{site.baseurl}}/images/create-gh-pages-branch.JPG)

Now, go to settings and check the **Github Pages** section. You should see a URL where the blog is hosted.

This process will host the theme as a **Project Page**. You can also download the files for local development. 

Default theme will look like this

![webjeda sidebar theme]({{site.baseurl}}/images/webjeda-sidebar-theme-screenshot-1.jpg)


# Customization

## Theme
The theme provides a nice sidebar that can be toggled using a menu button. It can be customized by changing colors in the **_config.yml** file.

{% highlight yml %}
#color scheme
sidebar-color: '#3A539B'       
accent-color: '#3A539B' 
{% endhighlight %}

![webjeda sidebar theme]({{site.baseurl}}/images/webjeda-sidebar-theme-screenshot-2.jpg)


You may have to sign up for google custom search engine and use the ```google-custom-search-cx``` code inside **_config.yml** file.

There are other things you may have to change

## Google analytics
Change the analytics ID in the **_config.yml** file. If you leave it blank, analytics will not run the code on any page.

## Disqus short-name
Sign up for Disqus, get the shortname and add it in the **_config.yml** file. If you leave it blank, disqus will not run on any page.

## Social media links
These links are basically designed for the footer. which I'm yet to design(under construction).

## Google custom search
Google custom search is the one I prefer over others because of many reasons.

1. It is free.
    
2. Provides accurate results.
    
3. No burden on hosting server.
    
4. Searching from multiple websites of yours is possible.
    
5. Google tracks the queries which can be helpful to optimize your blog.



# Development
Make changes to the **master** branch and create a pull request. Do not use **gh-pages** branch as it is used to host the theme.


# License
Copyright 2013-2015 Iron Summit Media Strategies, LLC. Code released under the [Apache 2.0](https://github.com/IronSummitMedia/startbootstrap-simple-sidebar/blob/gh-pages/LICENSE) license.