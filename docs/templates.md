# Competitive Container Templates

This example will explain the competitive container template through an example using a Jupyter notebook. In this scenario, you might want to choose this template for your competition if you want your users to (generally) stick to Python. 

## Creating a Competition
The basic steps for creating your own competition are as follows:

1. Setup a folder
2. Define your Competition
3. Add the download of your data to the build spec
4. Share it

## Participating in a Competition
1. Find a competition that you like (on a TBA search interface)
2. Pull the container
3. When you are done, submit your result with a tool built into the container

Let's start by talking about the Competitive Container templates

## Competitive Containers

### 1. Setup
Your competition is going to live in a container. Specifically for this example, we are going to be giving our users a jupyter notebook working environment (Python) so we start with that base. If you aren't familiar with Singularity, you build containers based on these recipes called [Singularity](http://singularity.lbl.gov/quickstart) files. Your competition container is going to be generated from such a recipe. You can either clone the repo to see the example template:

```
git clone https://www.github.com/containers-ftw/cftw
cd cftw/cftw/templates
ls

Singularity.jupyter
__init__.py
```

or just create your own folder, and get the Singularity file here for it:

```
mkdir mycompetition
cd mycompetition
wget https://github.com/containers-ftw/cftw/blob/master/cftw/template/Singularity.jupyter
```

### 2. Define your Competition
The template provided is empty, meaning that you start with the some base build recipe file, and tweak it to define your competition. If you haven't already, you should [install Singularity](http://singularity.lbl.gov/install-linux). We will have support for Docker for local analyses, but largely will be using Singularity in the case that users need to run and work in a shared environment. Let's take a look at an empty build spec file:

```
BootStrap: docker
From: continuumio/anaconda3

%runscript

     echo "Starting notebook..."
     echo "Open browser to localhost:8888"
     exec /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser

%post

     # Install jupyter notebook
     /opt/conda/bin/conda install jupyter -y --quiet 
     mkdir /data
     mkdir /opt/notebooks
     apt-get autoremove -y
     apt-get clean
```

If you are familar with jupyter, you might know what the above does. It installs jupyter notebook via an anaconda environment, and then runs it on port 8888 on your localhost. We store our notebooks in the directory `/opt/notebooks` in the container. In fact, we can build this container, right now, and use it for that! Here is how to do that, assuming `Singularity.jupyter` (the file above) is in the present working directory:

```
singularity create --size 2000 jupyter.img
sudo singularity bootstrap jupyter.img Singularity.jupyter
```

You are going to see layers for your image being pulled from docker, and then you will have it, a `jupyter.img` in your folder:

```
ls
jupyter.img  Singularity.jupyter
```

You can use your image by running it, and binding any directory with notebooks to `/opt/notebooks` in the container. Then open your browser to port 8888. 

```
singularity run -B $PWD:/opt/notebooks jupyter.img
```

### 2. Add your data
We are half way there! What we really want to do is have users grab our data when they create the container. Did you notice the `/data` folder that was created? You can put your data files there, in many different ways.

#### Adding local files
When you submit your recipe, it will be built and served on [Singularity Hub](https://www.singularity-hub.org), so it makes sense to start with your code (the build recipe and data files) in a Github repo. If you want to add local files, you can do that by way of a `%files` section in the recipe:

```
%files
data.csv /data/data.csv
training-labels.csv /data/training-labels.csv
```

The above build would work for a folder that looks like this:

```
/mycontainer
    Singularity
    data.csv
    training-labels.csv
```

and each of the data files would be moved inside the container.

#### Bigger Data
If you have larger data to disseminate, this is still an unsolved problem. You need to put it somewhere that is web accessible, and then in the `%post` section of your script, download it to data. That might look like this:

```
%post

cd /data
wget https://www.dropbox.com/user/myreallybigdata.tar.gz
tar -zvff myreallybigdata.tar.gz
```

In the above example, having this happen in `%post` will mean that the data is provided in the container. If your data is too large for a container, then you will want to give instructions to the participant on how to download your data (to their host) and then they will bind the container to the `/data` folder:


```
singularity run -B $PWD:/opt/notebooks -B $HOME/Downloads/data:/data jupyter.img
```

We will discuss instructions and interacting with data more in a bit.
