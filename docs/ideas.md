## Idea and Thinking Area


### Who hosts the competition board?
The challenge comes down to the hosting of the service that "collects and summarizes" the metrics. This means we need servers, and the need can be tackled in one of two ways:

 - **central provider**: this is based on the idea of having some central registry thing that users (interactively) use to create accounts, and then submit results (likely a link to a container build on Singularity Hub) via  a web interface. 
   - **pros**
       - it's a nice way to summarize across competitions
       - the central provider can manage the tool, improve or change it, respond to issues
   - **cons**
       - the researcher may feel less ownership over his/her competition
       - it makes it harder for customization, because the resource isn't controlled by the researcher

 - **individual providers**: this means that, when I want to host a competition, I am given a starting template that I can host on my own. 
   - **pros**:
       - I have ownership, and I am empowered to make changes
   - **cons**
       - It's harder to keep track, across competitions


After thinking about this, I like the idea better of making researchers empowered to host their own competitions, using tools that are already comfortable and familiar to them. One reason (of many) is that providing a service is a costly thing, and it's a lot of investment for one person or group. If the idea of containers-ftw is crowd sourcing, then the deployment of these competitions should be do-able by anyone.

**DEFINITIONS**: We will call the host of a competition the **provider**. The provider is likely the scientist that hsa a question, knows how to describe and measure it, and also knows how to assess the goodness of a result. It is the provider that is responsible for hosting the competition, and defining metrics for success. We will call the participant in the competition the **competitor**. The competitor minimal experience needs to be with using Github and some scientific programming.


### A Central Framework?
I had first thought about a framework that might look like this:

 - make your competitive container
 - add the build file to Github
 - build it on Singularity Hub
 - a static API from a **provider** github repo has the container registered via a PR, and the result is obtained from the Singularity Hub API (and we would need to add some functionality to a singularity hub builder to do this).

The problems I see with the above approach are that, even though Singularity Hub connects with Github, it's still a very far jump between the containers there and a Github repo. Singularity Hub also assumes that the container is there for someone to use via the singularity software, and it's not really a living thing. Arguably, we want a builder that is closer to the competition, and gives us more ability to specify what happens during the build. For this reason, 


### Competitive Containers via Continuous Integration
The builds would be better to happen with Continuous integration. By making it possible for a researcher to, by way of a simple Github repo, host, assess, and save all records of a collaborative effort? That sounds amazing. 


#### The Provider
Here is what that would look like, first for the **provider**:

 - make your competitive container, likely just from a provided template (from `cftw`)
 - data is added to the container via download or local files, along with other software dependencies.
 - the analyses (to produce output) will live in the `%post` too, and competitors provided with easy ways to generate this content (discussed below)
 - the `%test` section of the container, during CI, will run to assess the result (functions likely from cftw)
 - commit the build file, along with a standard CI config file to Github
 - the Github repo contains the entire history, and understanding of your question. You can use the README to describe things, the wiki, or any form of docs. All notes are version controlled and linked directly with a state of the competition.
when 
 - the repo also has a provided template that will serve it as a Github pages site, where people interested in your competition will read a (template produced) instructions of how to participate.
 - the cftw software will be the main driver of the CI
 - when your repo is ready for staring, you can share it with others, or (better) we will have some central place to link to it as a competition.


#### The Competitor
Now what happens if you are a **competitor**?

 - You browse to some central place of competitions (can even be static), or see a link on Twitter, you find it.
 - You fork the repo, and clone it to your computer, build and run the container.
 - You open the jupyter notebook, write some functions, and come up with a result
 - The container can (locally) be tested to assess if the result conforms to the required
 - You commit your changes, push to Github, and then do a PR to the main repo.

#### The PR
The cool thing about using Github and PRs is that the infrastructure is more in line with how science is - a scientific question can be a well defined thing with a metric for answering it, but the ways that we try to answer it, and the methods available to us, or even the data available, is a living and changing thing. 

 - I can stumble on a repo in 10 years, and still submit a new result toward the same metric
 - If a publication or written record is needed, you can have a way to combine discussion from pull requests, wiki/docs, and all products of the collaborative environment to give everyone credit. There are entire journals on Github, so it would be reasonable to wrap something like that into this.
 - When a PR is done, it creates the container in the CI to produce the result, and the result is evaluated. What the PR will basically do, if accepted, is:
    - add the container build file and it's result output to a folder to live forever with the repo. The author should be encouraged to write up some details of the analysis, although it's not required.
    - when the CI runs, it will run the metric to compare the result against the ones already there. The merged PR would then update the github page (web interface) associated with the repo, the "leader board."

With this kind of framework, collaboration just comes down to the standard workflow that most scientists are getting accustomed to. The cool parts (github pages, tools and helpers for CI) are provided by cftw.


##### Improvements over Publication
Right now we go through the pain of publishing and then put up the false idea that there is somehow a "finished result." Using continuous integration and PRs, I could have container competition that someone stumbles on in 10 years, and then can submit a new way to go about it, and either reproduce some finding or improve upon the metric of interest.  An analysis becomes a living thing that is recorded, and any single result or entire container is easy to reproduce, talk about collaboratively, or assess programatically. Someone could also stumble upon a competition repo, and do a meta analysis across all results, or even choose to build the containers and re-run them how they please.

#### Encouraging Sharing Analyses
This is also a cool approach because one repo is associated with a scientific question, a metric for assessing it, and containers that (each on its own) could be built to assess it (in all the different ways that people submit PRs to do).

This is along the lines of what I'm currently thinking.
