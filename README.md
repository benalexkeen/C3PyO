# WebJeda Sidebar Theme
Webjeda sidbar theme is based on Simple Sidebar theme by [Start Bootstrap](http://startbootstrap.com/). It is optimized to be used on Jekyll. 

![webjeda sidebar theme](/images/webjeda-sidebar-theme-screenshot-1.jpg)

# Installation
Fork the ``master`` branch and delete ``gh-pages`` branch. This is important because ``gh-pages`` branch is used here only to host the blog. You should be using master branch as the source.

## How to delete old ``gh-pages`` branch?
After forking the repository, click on **branches**.

![delete gh-pages branch](/images/delete-github-branch.png)

Delete ``gh-pages`` branch.
![delete gh-pages branch](/images/delete-github-branch-2.png)

You have to create a new ``gh-pages`` branch using the master branch. Go back to the forked repository and create ``gh-pages`` branch.

![create gh-pages branch](/images/create-gh-pages-branch.JPG)

Now, go to settings and check the **Github Pages** section. You should see a URL where the blog is hosted.

This process will host the theme as a **Project Page**. You can also download the files for local development. 

Default theme will look like this

![webjeda sidebar theme](/images/webjeda-sidebar-theme-screenshot-1.jpg)



## Customization
The theme provides a nice siebar that can be toggled using a menu button. It can be customized by changing colors in the **_config.yml** file.


      #color scheme
      sidebar-color: '#3A539B'       
      accent-color: '#3A539B' 


![webjeda sidebar theme](/images/webjeda-sidebar-theme-screenshot-2.jpg)


You may have to sign up for google custom search engine and use the ```google-custom-search-cx``` code inside **_config.yml** file.

## Development
Make changes to the **master** branch create a pull request. Do not use **gh-pages** branch as it is used to host the theme.

## Copyright and License
Copyright 2013-2015 Iron Summit Media Strategies, LLC. Code released under the [Apache 2.0](https://github.com/IronSummitMedia/startbootstrap-simple-sidebar/blob/gh-pages/LICENSE) license.
