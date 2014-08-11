select x.docid, y.docid, sum(x.count*y.count) as simi from (
(select docid, term, count from search
where docid='q') x,
(select docid, term, count from search) y)
where x.term=y.term
group by x.docid, y.docid
order by simi desc;