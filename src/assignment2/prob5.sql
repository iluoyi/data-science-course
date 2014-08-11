select count(*) from (
select docid, sum(count) as term_count from frequency
group by docid
having term_count > 300);