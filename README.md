# how-to-human-eval

## Introduction
This is a short tutorial on how to conduct a human study using Amazon Mechanical Turk and Google Drive. Specifically, I describe a workflow that caters to collection of human responses for 1000s of images/documents/videos or other media. If you are evaluating only on <10 items, don't even bother with this tutorial. 

Automated metrics are good to have -- they are easy and quick to use, cheap; but they are only a proxy for human evaluation. A human study is the gold standard for evaluating new proposals (algorithms, interfaces) in scientific fields such as computer-human interaction (CHI), Machine Learning, etc. The flipside is that human evaluation is very expensive and tricky to conduct. Some examples:
1. [CHI] You prototyped a tool that can help in editing podcast audio and transcripts. How do users interact with this tool -- what buttons do they click more often? Are they irritated by the transcript font?
2. [CV / ML] You designed a new image compression algorithm. Are users satisfied with the quality of reconstructions? 

Note that abstract notions such as "quality", "satisfaction", "irritated" cannnot be captured entirely by automated metrics. 

Designing questions is hard. Refer to this paper by [Abigail See et al. (2019)](https://arxiv.org/abs/1902.08654) for questionnaire design (ML / NLP perspective) and related video from [1:06:13](https://www.youtube.com/watch?v=4uG1NMKNWCU&list=PLoROMvodv4rOhcuXMZkNm7j3fVwBBY42z&index=15)

Proceed to [hueval_tut_git.pdf](https://github.com/suryabulusu/how-to-human-eval/blob/main/hueval_tut_git.pdf) for a detailed discussion on steps to conduct human study with MTurk + GDrive.

If there are any mistakes, suggestions, or improvements -- please create an issue or [contact me](mailto:teja.surya59@gmail.com). Thanks!

## MTurk

[Amazon Mechanical Turk](https://www.mturk.com/) (AMT / MTurk) is a platform that automatically connects researchers with a broad pool of annotators (MTurk Workers). It is great for quick expeirments/surveys, but if you wish to evaluate slightly complex systems (say a chatbot) with more fine-grained control on who your annotators are, check [simple-amt](https://github.com/jcjohnson/simple-amt). Note that MTurk is not a perfect platform --there are several [scientific](https://www.cloudresearch.com/resources/blog/superworkers-mturk-users-bias-sample/) and [ethical](https://restofworld.org/2021/refugees-machine-learning-big-tech/) concerns. 

[Crowd html](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html) elements from Amazon makes it very easy to prepare UI on MTurk.

## Why Google Drive (and this tutorial)?
I wanted to conduct an experiment to evaluate how well a new image compression algorithm performs -- did users find the reconstructions of **our** new algorithm better, as compared to baseline (say, HiFiC) algorithm. 

MTurk does now allow images to be uploaded. I have to provide **public URLs** of the images to display them to annotators during the survey. An easy way to obtain public URLs of the images is by uploading them to Google Drive (or Dropbox) and making them shareable. This creates a public URL which enables anyone on the internet to view, which can be readily used on MTurk. Sounds good, right?

Not really. Uploading images to GDrive is quick, but how do I manually copy public URLs of **1000s of images**? This is where [PyDrive](https://pythonhosted.org/PyDrive/) comes in. PyDrive library provides tools to iterate over entire GDrive and extract public URLs. It comes with some caveats (as of March 2022) such as not being able to iterate over specific folders -- but its incredibly quicker than manually copying URLs.

[public_urls_colab.py](https://github.com/suryabulusu/how-to-human-eval/blob/main/public_urls_colab.py) contains ~25 line python code that has to be run on [Google Colab](https://colab.research.google.com) to prepare URLs for images. Further description is in the tutorial pdf. 

**Why this tutorial?**: It took a while for me to figure out how to enable this workflow of going from GDrive to MTurk. There are lots of scattered helpful tips on [stackoverflow](https://stackoverflow.com/questions/40224559/list-of-file-in-a-folder-drive-api-pydrive) and other blogs. I have just compiled all tips that worked for me in this repo -- there is absolutely nothing new I added. 

## Folder Structure
* `exp{i}.html`: UI that is displayed to annotators. Name `class` and `id` elements carefully as they will later be very useful during analysis of results.
* `exp{i}_full.csv`: list of images and their properties that help in populating the UI. These are intermediate files since they contains no public URLs. Once the public URLs are available, these files can be converted to `exp{i}_fullurl.csv`.
* `exp{i}_fullurl.csv`: same as the previous set of files with additional columns containing public URLs of images. These files get uploaded to MTurk and each row is interpreted as a [HIT](https://www.mturk.com/worker/help). 
* `exp{i}_small.csv`: These files can be uploaded to conduct a small **pilot study**. Pilots are immensely useful because they provide a cheap and quick feedback as to how the annotators are interpreting the questions you've asked. You can improve the UI / questions before the full study is conducted. 
* `imgcomp_urls.json`: Exapmle json dict file with image name as key and its public URL as value. 
* `exp1_results.csv`: Sample results of Experiment 1. Notice the column names and comments.  

## Final Comments
1. Since we cannot iterate over specific folders with PyDrive, carefully name image files before uploading to GDrive, especially if they are split over multiple datasets and categories. Check tutorial pdf for example. 
2. Add sanity check questions -- this will help in accepting / rejecting responses. 
3. Examine the amount of time annotators are taking to complete the survey. Try out several HITs on your end before publishing survey. 
4. The number of images/items over which you are evaluating depends on your budget. Please plan budget carefully and pay annotators well. I provided some pointers on how to plan budget in pdf. 
5. I have no idea why residents of India cannot create MTurk Requestor accounts. Find people in the US who can set up an account on your behalf. Payment is also confusing to me.

<img width="1523" alt="image" src="https://user-images.githubusercontent.com/21237473/156382657-5d2026bc-db85-43e6-b537-624699660ea5.png">





