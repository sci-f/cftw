# Containers, For the Win!

If reproducibile science is hard, this suggests that maybe the old fashioned way of "protect your data and ideas, and hand the secrets only over to your three graduate students" might not be the best strategy anymore. In an effort for open, and collaborative science, we present containers for the win. This effort is based on the following ideas, in no particular order:

 - Discovery, and asking important questions is the gut of science, and everything must go towards supporting that.
 - The burden of perfection for computational excellence on the sole researcher is asking too much. Science is a team effort involving domain experts, computational scientists, and software engineers. All parties involved should be able to focus on their expertise and interest.
 - Thus, a researcher should be able to develop a reputation based on carrying out an experiment exhausteively, at scale, and with impeccable technique. A software engineer should be able to contribute by publishing robust tools, data standards, and analysis protocol or pipelines.

It follows logically that, if scientists are able to define specific computational experiments and metrics for success, and tools exist that empower the scientist to share experiment definitions, crowd sourced science is simply a matter of sharing your experiment with others, and giving them an easy way to submit and then evaluate a result. 

## Collaborate on Reproducible Containers
By way of container technologies like [Singularity](http://singularity.lbl.gov), we can now use containers on shared computational resources. This means that, if a scientist is given the tools to package data, a means to transport dependencies and submit results, and a metric of evaluation, dissemination of the entire experiment comes down to sharing a build recipe for a container. Submitting a result comes down to a user putting his or her code into the container, and then sharing it. These are indeed containers ftw, because each has a well defined question, and a metric of success.


## cftw
This base repo, a module called `cftw` will provide command line functions for doing the following:

 - generating container templates to share
 - submitting them (possibly via Github) to the larger community
 - interacting with a simple web application to collect results from users

We don't anticipate asking the user to need to install the module directly on his or her system, it will be packaged in the container recipes that he/she users to generate the final result. Templates (e.g., bases for different kinds of analyses, like providing a jupyter notebook) can be programatically obtainable with this softare, but they can also be downloaded or copy pasted directly from Github. This documentation base will review the following:


 - [Getting Started](getting-started.md): This is an overview of getting started on generating a container. We will define a container to perform linear regression, six ways.
 - [Competition Server](): This (will be) documentation for how to host a simple competition. We plan to provide this interface for you, but you are free to deploy it yourself.
 - [Submitting an Entry](): This will review how to browse and find competitions of interest, and submit an entry.
