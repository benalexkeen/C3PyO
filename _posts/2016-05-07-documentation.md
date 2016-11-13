---
layout: post
title: Documentation
---

* Do not remove this line (it will not be displayed) 
{:toc}

# Features

## Customizable theme
The theme can be customized just by changing few variables in **_config.yml** file.

## Inline CSS
Since the style used in this theme is very less, I'm inlining it. This will save a request and hence speeds up website loading.

## Light-weight
Since the theme is based on default Jekyll theme, it is very light-weight. No JavaScript except analytics is used!
![jekyll theme thunder speed test]({{site.baseurl}}/images/webpagetest-jekyll-theme-thunder.jpg)

## Prose editing ready
You can edit or add blog posts easily using [Prose](http://prose.io).

## Pre-installed Disqus comments
Disqus is already installed. All you have to do is to sign up with Disqus, get the **disqus-shortname** and update it in the **_config.yml** file.

An example page loads completely in 1.1s!

In a comparision, it loads faster than an amp page made using Jekyll - [amplify](https://cdn.ampproject.org/c/s/ageitgey.github.io/amplify/2016/03/08/example-post.html){: rel="nofollow"}.

[Amplify page](https://cdn.ampproject.org/c/s/ageitgey.github.io/amplify/2016/03/08/example-post.html){: rel="nofollow"} loading speed
![Amp page loading speed]({{site.baseurl}}/images/webpagetest-jekyll-theme-amplify-example.jpg)


[Thunder page](http://webjeda.com/thunder/example/) loading speed
![Thunder page loading speed]({{site.baseurl}}/images/webpagetest-jekyll-theme-thunder-example.jpg)

Though the contents of the page are different, they are comparable because both pages have one image and thunder example has code, blockquote, table ordered list, unordered list and all headers. That I think is a fair comparision.




# Installation
Fork the ``master`` branch and delete ``gh-pages`` branch in it. This is important because ``gh-pages`` branch is used here only to host the blog. You should be using the master branch as the source and create a fresh ``gh-pages`` branch.

## How to delete old **gh-pages** branch?
After forking the repository, click on **branches**.


![delete gh-pages branch]({{site.baseurl}}/images/delete-github-branch.png)

Delete ``gh-pages`` branch.
![delete gh-pages branch]({{site.baseurl}}/images/delete-github-branch-2.png)

You have to create a new ``gh-pages`` branch using the master branch. Go back to the forked repository and create ``gh-pages`` branch.

![create gh-pages branch]({{site.baseurl}}/images/create-gh-pages-branch.JPG){: style="border: 1px solid #eee" }

Now, go to settings and check the **Github Pages** section. You should see a URL where the blog is hosted.

This process will host the theme as a **Project Page**. You can also download the files for local development. 

Default theme will look like this

![webjeda thunder jekyll theme]({{site.baseurl}}/images/thunder-jekyll-theme.jpg)

This theme is responsive.

![webjeda thunder jekyll responsive theme]({{site.baseurl}}/images/thunder-responsive-jekyll-theme.jpg)
{: style="text-align:center" }

# Customization

## Theme
The theme provides a nice header that can be customized by changing colors in the **_config.yml** file.

{% highlight yaml %}

#color scheme
color-1: '#E64C3C'
color-2: '#F0C419' 

{% endhighlight %}

![webjeda sidebar theme]({{site.baseurl}}/images/thunder-jekyll-theme-2.jpg)

Remember, while developing locally, every change you make in **_config.yml** is applied only if you restart ``jekyll serve`` process.

## Font 
The default font is Helvetica. Text shadow is used to give it a little deapth.

## Logo
The **webjeda thunder** logo is an SVG file. This can be removed and text can be used as the logo. Make these changes in the **header** file. But I suggest to use an SVG or an image.

# Development
Make changes to the **master** branch and create a pull request. Do not use **gh-pages** branch as it is used to host the theme.

# License
MIT License

# Changelog
<pre>
version 1.0 - Color-bar is now css. SEO improvements. Added an author section.  
  
version 0.9 - Minimal design, small and compressed css, built in disqus comments, compressed html, superfast loading UI.
</pre>