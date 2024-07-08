with text as ( -- trying to figure out the categories of action by verbiage of the first 3 words
  SELECT 
    split(latestAction_text, ' ')[0] || ' ' ||
    split(latestAction_text, ' ')[1] || ' ' ||
    split(latestAction_text, ' ')[2] category
  FROM `mlabs-incubator.skills_martinez.bills`
)
select category, count(category) from text group by 1 order by 2 desc

-- see if they're all from the 118th congress- about 2/3rds are from the house vs senate
select 
  congress, originChamber, count(congress) 
from `mlabs-incubator.skills_martinez.bills` 
group by 1, 2 order by 3 desc

-- select -- seeing the count of type
-- type, count(type)
-- from `mlabs-incubator.skills_martinez.bills`
-- group by 1 order by 2 desc

-- updates tend to happen on... friday
select
extract(dayofweek from updateDate) weekDay, count(updateDate) updates
from `mlabs-incubator.skills_martinez.bills`
group by 1 order by 2 desc


