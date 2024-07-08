# Submission - Anthony Martinez



## Queries

(Source code is included as a plain SQL file in repository.

### Breakdown of bills in the House vs Senate
I want to see a simple breakdown of bills: does one chamber work on more bills than the other? We actually see that the House deals with twice as many bills as the Senate- this makes sense: more members and more sponsors dealing with all sorts of government initiatives. 
```
-- see if they're all from the 118th congress- about 2/3rds are from the house vs senate.

select

	congress, originChamber, count(congress)

from  `mlabs-incubator.skills_martinez.bills`

group  by  1, 2  order  by  3  desc

```

### What dates do updates happen?
We have some limited data on the dates that bills are updated, so what day of the week do these latest updates typically happen on? Perhaps this could shine a little insight on working patterns in congress. We don't see any major trends, though it seems that updates tend to happen at the end of the workweek.  
```
-- updates tend to happen on... friday! slightly more than any other day. 

select

extract(dayofweek  from  updateDate)  weekDay, count(updateDate)  updates

from  `mlabs-incubator.skills_martinez.bills`

group  by  1  order  by  2  desc
```

### Categorizing the verbiage of the action text
I wanted to see if most actions fit into a few specific categories, or if they were all somewhat unique. In these results we do see that over 70% have to do with referring bills to relevant committees (sometimes after reading them twice).

```
with  text  as  (  -- trying to figure out the categories of action by verbiage of the first 3 words

SELECT

split(latestAction_text, ' ')[0] || ' ' ||

split(latestAction_text, ' ')[1] || ' ' ||

split(latestAction_text, ' ')[2]  category

FROM  `mlabs-incubator.skills_martinez.bills`

)

select  category, count(category)  from  text  group  by  1  order  by  2  desc
```

## Ways to improve

1. I'd definitely love to expand our data set: instead of only 1000 or so bills, try and quickly see if it's feasible to get 5 years of data- with relevant amendments and hearing data using the other relevant endpoints. 
2. Depending a little on [1], I anticipating needing to potentially architect things a little more on dates: how do amendments and updates relate to the rows in each of the tables ? Ideally, I would desire to have as an table where one row is an "action", which could be grouped up and analyzed by bill (specifically bill number). The "latest action" dates in the bill table are nice but limits our potential conclusions without data about the intermediate steps. 
3. If I had the capacity to keep on after these steps, I'd love to analyse the text of the titles and actions themselves. A quick version would be to have binary features based on if a particular keyword is in the text (e.g. "referred to committee" by literally seeing if that is a substring in the action text), for a few dozen different phrases- a potential future step is using some more powerful text tools, such as NLP packages in python or R.