
# Data Scinece course on Coursera
# @author Yi Luo

# load the data
seaflow <- read.csv(file="seaflow_21min.csv",head=TRUE,sep=",")
summary(seaflow)

# partition the data into training/testing sets
library(caret)
trainIndex <- createDataPartition(seaflow$pop, p = .5,list = FALSE,times = 1)
seaflowTrain <- seaflow[ trainIndex,]
seaflowTest <- seaflow[-trainIndex,]
qplot(seaflow$pe, seaflow $chl_small, col=seaflow$pop)

# train the normal decision tree
library(rpart)
fol <- formula(pop ~ fsc_small + fsc_perp + chl_small + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data= seaflowTrain)
print(model)

preResults <- predict(model, newdata=seaflowTest, type="class")
prob <- sum(preResults == seaflowTest$pop) / nrow(seaflowTest)

# train the random forest model
library(randomforest)
model2 <- randomForest(fol, data= seaflowTrain)
preResults2 <- predict(model2, newdata=seaflowTest, type="class")
prob2 <- sum(preResults2 == seaflowTest$pop) / nrow(seaflowTest)
importance(model2)

# train the svm
library(e1071)
model3 <- svm(fol, data= seaflowTrain)
preResults3 <- predict(model3, newdata=seaflowTest, type="class")
prob3 <- sum(preResults3 == seaflowTest$pop) / nrow(seaflowTest)

# confusion matrix
table(pred = preResults, true = seaflowTest$pop)