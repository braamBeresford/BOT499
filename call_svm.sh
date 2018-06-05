set R_LIBS $R_LIBS\:/local/cluster/R_Packages/3.3

class1Examples=./data/features/features.merged.1
class2Examples=./data/features/features.merged.2

Rscript quick_svm.R $class1Examples $class2Examples
