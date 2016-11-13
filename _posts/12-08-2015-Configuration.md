---
layout: post
title: Configuration
category: docs
excerpt: Configure Algomash to make it yours
---

## Algomash is easy to configure
{: .content-subhead }

Once you've downloaded the Algomash, unzip it into the directory you would like to work. If you already know Jekyll that's great. Even if you don't, I'll walk you through this.

## Rename Directory
{: .content-subhead }

You can rename the directory to anything. Instead of `algomash-jekyll` you can use `my-cool-project` or anything you like.

## congif.yml
{: .content-subhead }

Open `config.yml` file from the folder into a code editor. You can also drag the folder into a code editor, as it'll be easier to work with.

In this file under the `## Setup` (line 9), you'll find 5 settings. That's all you need to configure.

* **title**: Change it to your site's title. You can use your project name if you wish.
* **tagline**: Change it to your site's tagline. A one line description would be sufficient.
* **description**: Change it to your site's description. This text is used in meta description tag in page header.
* **url**: Change this to your site URL. If you're developing locally on your machine for now, use **http://localhost:4000** as this is where Jekyll will run the server.
* **assets**: By default, Algomash uses a folder with name `assets` where all the resources like CSS, JS and images are stored in respective directories. You can rename the folder to something else, like `data` if you want. Also, update the site URL here too.

## Add Google Analytics Code
{: .content-subhead }

You can add Google Analytics tracking code in `_includes/google-analytics.html` file.

## Start the server
{: .content-subhead }

Now with the basic configurations done, start the Jekyll server. You can do this by:

* Open a Command Prompt or Terminal.
* Navigate in your site directory like `Documents\Codes\my-cool-project`.
* Run the command: `jekyll serve`.
* Open a web browser and navigate to **http://localhost:4000**.

See the Algomash site? Cool! Now what? Add the content, customize the CSS and host it somewhere.

For more advanced configuration, visit [Configuration page on Jekyll](http://jekyllrb.com/docs/configuration/).