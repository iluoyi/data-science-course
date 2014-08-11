select sum(x.count*y.count) from (
(select term, count from frequency
where docid='10080_txt_crude') x,
(select term, count from frequency
where docid='17035_txt_earn') y)
where x.term=y.term;