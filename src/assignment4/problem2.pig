fs -mkdir /user/hadoop

register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- DEBUG: raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

subjects = group ntriples by (subject) PARALLEL 50;

count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

counts = group count_by_subject by (count) PARALLEL 50;

histogram = foreach counts generate flatten($0), COUNT($1) as count PARALLEL 50;

-- DEBUG: store histogram into '/tmp/finaloutput' using PigStorage();
store histogram into '/user/hadoop/problem2' using PigStorage();
