fs -mkdir /user/hadoop

register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- DEBUG: raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- DEBUG: filtered = filter ntriples by subject matches '.*business.*';
filtered = filter ntriples by subject matches '.*rdfabout\\.com.*';

copied = FOREACH filtered GENERATE subject as subject2, predicate as predicate2, object as object2; 

-- DEBUG: joined = join filtered by subject, copied by subject2;
joined = join filtered by object, copied by subject2;

results = distinct joined;

-- DEBUG: store results into '/tmp/finaloutput' using PigStorage();
store results into '/user/hadoop/problem3' using PigStorage();
