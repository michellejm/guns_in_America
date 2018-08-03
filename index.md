# A Distant Reading of Politically Polarizing Events: Topic Modeling US Media Coverage

## A Polarized Landscape 

The United States is going through an unprecedented period of political polarization that is unprecedented in recent history, and has been increasing over the past twenty-five years. This polarization is not limited to our elections, but can can be seen on [college campuses](https://www.washingtonpost.com/news/rampage/wp/2017/05/02/political-polarization-among-college-freshmen-is-at-a-record-high-as-is-the-share-identifying-as-far-left/?utm_term=.ec991372a6de), in the [workplace](https://hbr.org/2017/05/research-political-polarization-is-changing-how-americans-work-and-shop), and in the [media we consume](http://www.journalism.org/2014/10/21/political-polarization-media-habits/). In many ways, this is a self-fueling effect: the more polarized our opinions become, the more we produce and consume media that align with our own ideologies, unwilling or unable to see or understand the other side without our own implicit or explicit biases.
 
Given this state, I wanted a way to compare media that is consumed by people at both ends of the political spectrum. Understanding that I would bring my own implicit biases to any actual reading, this project seeks to distill the articles into topics and narrative styles that can, [from a distance](https://www.nytimes.com/2011/06/26/books/review/the-mechanic-muse-what-is-distant-reading.html), be compared and understood. It is my hope that this will make it possible to see both the most contentious points as well as the areas of agreement and shared values.

For this initial exploration, I focused on the debate around gun control. The project started in the days after the Parkland shooting, and includes articles going back to Sandy Hook. The results show that across the political spectrum, people care about many of the same things: legal issues, gun sales, the opinion of those who operate firearms for their work, etc. Almost every media outlet used language to emphasize that their opinion is the best. However, the appearance of three topics in particular were divided along political lines: articles about research, mass shooting incidents, and those that explicitly contradict the opposition. The findings offer insight into why and how the political poles are talking past each other. 

## Methods

To collect the data for this project, I identified 10 representative media outlets drawn from a combination of this 2014 [Pew Study](http://www.journalism.org/2014/10/21/political-polarization-media-habits/) of the political polarization of American media, and this 2017 [Medium post](https://medium.com/@jeffjarvis/a-proposal-to-start-a-responsible-reliable-reasonable-conservative-news-organization-b0dfb60312c7) by CUNY Journalism Professor, Jeff Jarvis. There were not enough conservative media outlets to choose from in the Pew Study, and conservative media has started to expand since the Pew Study was conducted, so the Jarvis article was referenced. Infowars and the Nation were both choosen because they were referenced in that article. The Pew Study is concerned with what media people consumes and how participants rated the trustworthiness of each outlet. They asked about personal political affiliation and what media they consumed for political and current events.  Therefore, this is a study of how the people who consume the media identify rather than the political position of the source itself. 

The media outlets are:

Liberal:
NPR, New York Times, MSNBC, Huffington Post, and the Nation

Conservative:
Wall Street Journal, Fox News, Breitbart, the Blaze, and Infowars

Furthermore, it should be noted that conservative-identified respondents rely on Fox News more than any other source whereas liberal-identified respondents reported drawing on multiple different outlets. This may introduce some bias with respect to how influential each outlet is for different groups. However, in an attempt to capture the polarization of the conversation, the influence each outlet contributes to the total is unweighted.

The outlets were ranked based on degree of polarity, degree or trust, and a composite ranking. For polarization, a 5 is very polarized because they are consumed by "consistent conservatives" or "consistent liberals" and a 1 is consumed by people who identify as more central. The degree of trust was similarly ranked, where 5 is more trusted than distrusted and -5 is more distrusted than trusted. 

Finally, I calculated an overall rating by subtracting the polarity from the trust. Using this metric, the Wall Street Journal has the highest rank (it is the least polar and most trusted by the widest range of people) followed by NPR because they are widely trusted and are read by more central audiences - they are more trustworthy than polarizing. InfoWars has the lowest score followed by the Nation because they are both read by highly polarized audiences though they are not widely trusted even by some people who identify with their polar skew.

The Blaze and New York Times (NYT) are similarly ranked, even though the Blaze is read by more polarized readers than the NYT. Their ranking is in part because consistently conservative readers trust the Blaze and distrust the NYT whereas the opposite is true for consistently liberal readers. The result is that the mid-range media sources are the Blaze, NYT, and Fox News.  


| Outlet	| Trust  | Polarity  | Rank |
|:---------:|:------:|:---------:|:----:|
| WSJ	    | 4	     | 1	     | 3    |
| NPR		| 5	 	 | 4		 | 1    |
| MSNBC		| 1		 | 1		 | 0    |
| Blaze		| 3		 | 4		 | -1   |
| NYT		| 2		 | 3		 | -1   |
| Fox		| -1	 | 2		 | -3   | 
| Breitbart	| -2	 | 3		 | -5   |
| huffPo	| -3	 | 2		 | -5   |
| Nation	| -4	 | 5		 | -9   |
| InfoWars	| -5	 | 5		 | -10  |


While this ranking has its own significant bias in it, it offers a useful way to rank the combination of how much each outlet it trusted across a polarized audience. This is not to say that any outlet **should** have any particular ranking, only that within this ecosystem, this is what the composite trust/polarity 


### Collecting the Corpus

Once the outlets were identified, I made Google [Custom Search Engines (CSE)](https://cse.google.com/cse/all) for each source so I could get lists of article links for each source. I then made a list of keywords related to gun control. I looped through this list on each CSE to get a list of article links (omitting duplicates).

The Gun Control Keywords are: gun, firearm, AR15, AR-15, weapon, shot, shoot, rifle, bump stock. Since these were used in the CSE, it collected any article that mentioned one of these words. As a result, there were articles about flu shots, weapons in North Korea, Syria, and Turkey, and similar topics were not related to gun control in the US. Since this is a rather short and finite range of other topics, any article about the flu or geopolitics was removed with list comparisons.

I then gathered the Title, Author, Date, and article content from each article using a combination of Beautiful Soup and Newspaper packages in Python.

### Topic Modeling

Once the corpus was collected, I transformed each article into a word vector that could be quantitatively analyzed. The first step was to remove the stop words. Stop words are functional words that are semantically opaque (though they provide a lot of syntactic glue), such as prepositions, auxiliaries, articles, etc. For example, if I want to tell you "the house is burning", you would know what I meant if I just said "house burning". Stop words don't contribute much meaning to the sentence, they make our algorithms run slower, and can through off identifying the topic since gender and genre affect the number of stop words. But after removing the stop words, there is still some cleaning to do to transform the sentences in our articles into a "bag of words" that the computer can analyze. First, I normalized the words by transforming them into lower case and removing punctuation. Then I lemmatized the words, transforming them into the appropriate roots (removing the grammatical affixes and finding dictionary forms). These steps are essential to minimize redundancy and maximize efficiency by ensuring that each word is content-ful and unique. Finally, we, as humans, are very good at understanding sentences and finding meaning amidst language, computers are better at statistics. So, to get the computer to interpret an article, it relies on the semantic content of the words, and nothing else. From here, I had to make a decision if I was going to use Non-Matrix Factorization (NMF) or Latent Dirichlet Allocation (LDA) because it affects the next step. LDA is a statistical model that utilizes a count vectorizer whereas NMF utilizes tf-idf - explained below. I ended up doing it both ways and picked the route with the more interpretable topics. The topics that appeared in NMF were more easily interpretable and quantifiable. 

The next step was to transform the list of words in each article into a series of vectors representing the article in relationship to the corpus. For example, let's say we have three articles. The first is about "the second amendment and the right to bear arms." The second is about "gun control and concealed carry laws." The third is about "the guns used in the Parkland shooting." For the purposes of demonstration, pretend that those quotes are the only words in each article. If we remove the stop words, normalize our words, and lemmatize them, our three articles now look like this:

1. second amendment right bear arm

2. gun control conceal carry law

3. gun use parkland shoot

Across our entire corpus, we have 13 unique words. We can transform each article into a vector, and the corpus into a matrix by assigning a 0 or 1 if the word appears or not. 

second, amendment, right, bear, arm, gun, control, conceal, carry, law, use, parkland, shoot

1. [1,1,1,1,1,0,0,0,0,0,0,0,0]

2. [0,0,0,0,0,1,1,1,1,1,0,0,0]

3. [0,0,0,0,0,1,0,0,0,0,1,1,1]

However, this too is a simplification. The bag of words statistic is actually created through a scoring metric called term frequency-inverse document frequency (tf-idf). Tf-idf is a non-binary statistic that represents the importance of a given word to the meaning of the article. This number increases every time a word appears in the article relative to the corpus. So, if a word is very common across all articles, its value in a tf-idf is low, whereas if a word appears many times in one article, but infrequently across the corpus, its value will be high. 

The sci-kit learn package for Python has a function to perform this, called tfidfvectorizer. I used this, and set the parameters to max_df = 0.9, min_df = 0.1, and removed the stop words. The min and max df here refer to how the vocabulary is built. For the max_df, the closer a term frequency is to 0, the more likely that a word is common. In this corpus, a word like "gun" likely has a term frequency very close to 0. In a study of gun control, the word "gun" doesn't tell us very much about the article topic because it likely appears in all of the articles. Therefore, I omitted anything with a term frequency less than 0.1. Likewise, any word that is very rare likely doesn't tell us much either. Even when an article is about a very specific topic, that word is likely to appear multiple times. Such a word may be a quirk of the author's style or a typo. Therefore, I omitted anything with a term frequency greater than 0.9.

This matrix forms the basis of the Non-negative Matrix Factorization method of topic modelling. The values from the tf-idf are transformed to produce topics. 

### Identifying topics

After some tinkering, I chose 24 topics with 2 words and then 10 words each. After 24, the topics started to be uninterpretable, and with fewer than 10 words, it's difficult to determine exactly what the topic was about. I then interpreted each topic based on my own understanding of the events and the discourse around gun control, I grouped them into broad categories and more narrow ones. The broad categories are: culture, incidents, legal issues, government, gun type, gun control, and sales. Though gun control is a legal issue, there are some legal issues that are distinct from gun control. 
 
Without human interpretation, these topics are meaningless, but this is also one junction where bias is often introduced. I then categorized each topic into a general category for analysis. For example, I classified Topic 0 as an 'incident', specifically, 'Parkland'. The 2 word version of Topic 0 is [shooting, mass], which tells us it was a mass shooting, but not which one. The 10 word version is [shooting, mass, people, florida, parkland, left, dead, two, victim, shooter], which tells us that this topic refers to the mass shooting in Parkland Florida. Some words are still so general that they are not helpful in figuring out what the topic is (i.e., 'people', 'left'), and these words probably could be removed with the stop words, but they also don't detract, so we won't worry about them.  The results are in the table below.

| Topic |	ten words                     | words2        | general      | specific        |
|:-----:|:-------------------------------:|:-------------:|:------------:|:---------------:|
| 0	    | shooting mass people florida parkland left dead two victim shooter            | shooting mass | incident	   | parkland        |
| 1	    | officer police department incident county city say video enforcement call	    | officer police| incident 	   | police shooting |
| 2	    | ar 15 semi used store buy automatic rifle ammunition gun	                    | ar 15	        | guns	       | ar 15           |
| 3	    | school student high parkland florida medium child control week national	    | school student| incident	   | parkland        |
| 4	    | trump president white house read morning republican wednesday lawmaker support| trump president| government  | trump           |
| 5	    | nation action sign take support issue three policy program matter	            | nation action	| culture	   | national identity|
| 6	    | say one like people think know would may could time	                        | say one	    | meta	       | opinions        |
| 7	    | gun control violence law owner show crime america say debate	                | gun control	| gun control  | national identity|
| 8	    | get news whether already sign read told life let follow	                    | get news	    | meta	       | meta            |
| 9	    | ban assault magazine weapon bill ammunition high bullet would president	    | ban assault	| gun control  | bans            |
| 10	| video street 000 country want people show world earlier across	            | video street	| incident	   | video           |
| 11	| state law carry bill legislation republican would measure lawmaker enforcement| state law	    |gun control   | legal           |
| 12	| firearm ammunition federal act gun sale use report crime owner	            | firearm ammunition| guns	   | ammunition      |
| 13	| com second amendment twitter news follow armed bullet medium host	            | com second	| gun control  | second amendment|
| 14	| rifle automatic military round semi assault fire style magazine long	        | rifle automatic| guns	       | assault weapons |
| 15	| said told county home authority official year two old according	            | said told	    | meta	       | meta            |
| 16	| new york city year morning old time law week first	                        | new york	    | incident	   | shooting        |
| 17	| background check sale system purchase gun record buy federal criminal	        | background check|	gun control| background check|
| 18	| court federal case right law family arm amendment second state	            | court federal | gun control  | second ammendment|
| 19	| nra national association member group republican right president political amendment|	nra national| gun control| nra           |
| 20	| weapon read 2016 use used system military assault report made	                | weapon read   | guns	       | assault weapons |
| 21	| company sale store year make group million end asked said	                    | company sale 	| guns	       | sales           |
| 22	| attack american government left report military official used member including| attack american| culture     | government      |
| 23	| shot man killed read year police old morning two 2016	                        | shot man	    | incident	   | mass shooting   |

### Analysis 

#### Topic Modeling

I then tallied what percentage of each general topic dominated each type of outlet, and what specific topics were the most explored by each media source. I further looked at what specific topics were the most polarizing from liberal to conservative, and investigated the coverage of both specific topics and general topics based on the trust/polarization score of each outlet. The results follow.

#### Sentiment Analysis

I then analyzed the sentiment of the first sentence of each article using [TextBlob's](http://textblob.readthedocs.io/en/dev/index.html) built-in, pre-trained [Sentiment Analyzer](http://textblob.readthedocs.io/en/dev/api_reference.html#module-textblob.en.sentiments). This classifier was trained on movie reviews and uses Naive Bayes classification. I needed a classifier that was trained on a different corpus because in our current political climate, I felt it would be nearly impossible to efficiently classify sentences without reifying the implicit bias I am attempting to address. Furthermore, I am biased. I know this about myself, and I also know that the majority of people I have contact with are biased in the same or opposite way. So I used a classifier that had already been trained on a different corpus. This may make the analysis weaker. However, it does allow me to have a supervised classification task without an annotated corpus. 

I then looked at the sentiment over time and by each topic, each media outlet, and against the trust/polarity scores.

## Results

### Topic Modeling

Overall, there was very little difference in coverage of each general topic by Conservative versus Liberal media outlets. The treemaps below illustrate the small differences. 

![Conservative Treemap](Conservativetreemap.png)

![Liberal Treemap](Liberaltreemap.png)

If instead we look at each topic along the degree of polarity, some interesting patterns emerge. Each of these graphs shows the prominence of the topic in each media outlet - ranked from those with a "consistently Conservative" readership to "consistently Liberal" (again, topics consisting of metadata or positional language (believe, said, etc.) were omitted. The order of outlets is:

Infowars, Blaze, Breitbart, Fox, WSJ, MSNBC, Huffington Post, NYT, NPR, The Nation

![small multiples: topic by polarity](cons-to-lib-all.png)

For the most part, the topics are relatively consistently spread across the political spectrum, though two topics stand out: Trump and videos. The first is the topic about Trump. We already know that Trump is polarizing as a topic, but it also seems that some outlets cover him with relationship to gun control. Interestingly, those outlets are neither all liberal nor all conservative, but rather spread throughout. The second topic is the one about video cameras. At first, I thought this was about body cameras, but it is actually related to reporting on video footage from protests and other events. For example, many of the articles that contributed to this topic were about the Chalottesville "Unite the Right" protest in August 2017, where many self-identified white nationalists chose to carry guns, and there was significant reporting on the video footage that counter-protesters and others captured. What is interesting about this topic is how erratic it seems when viewed along a political continuum. 

Some topics that we might have expected to appear differently in each media outlet do: the topic relating gun control and national identity is covered more broadly by conservative outlets than liberal ones, and the topic about culture and national identity shows the opposite trend. 

If we look at this same data organized instead by ranking (a composite of degree of polarization and degree of trust). Both of these topics (Trump and video coverage) are almost ignored by the outlets that are low polarization/high trust and high polarization/low trust, but were very widely covered by the outlets ranked in the middle. 

![small multiples: topic by ranking](rank-all.png)

The gun control and national identity topic seems relatively consistent across rankings, but a new topic appears: one of the assault weapons topics is more prominent in the higer ranked outlets (low polarity/ high trust). This is the topic that discusses rifles extensively (rifle automatic military round semi assault fire style magazine long), explaining the relationship between "military-style assault rifles" and "semi-automatic rifles". The other version of this topic, which is consistent across media outlets focuses more on the weapons aspect of these types of guns. 

If we look at the topics in terms of standard deviation to again identify those topics that are covered the most/least by different outlets, the same topics appear:

* Trump
* Gun control and the national identity
* Coverage of videos shared on social media

While these three topics do not seem to be, in and of themselves, able to account for the political polarization, they do seem to be adding to the ways in which the discussion diverges among self-selected groups. That is, some outlets cover these topics extensively, while others nearly avoid them - at least to a greater degree than other topics in the corpus. 

#### Sentiment Analysis


