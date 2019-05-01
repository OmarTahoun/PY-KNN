dataset <- read.csv("data.csv")
new_point <- c(5,7)


KNN = function(x,y,k=5)
{
  if (!is.matrix(x))
  {
    x = as.matrix(x)
  }
  if (!is.matrix(y))
  {
    y = as.matrix(y)
  }
  my_knn = list()
  my_knn[['points']] = x
  my_knn[['value']] = y
  my_knn[['k']] = k
  attr(my_knn, "class") = "my_knn_regressor"
  return(my_knn)
}

compute_pairwise_distance=function(X,Y)
{
  print(X)
  print(Y)
  xn = rowSums(X ** 2)
  yn = rowSums(Y ** 2)
  outer(xn, yn, '+') - 2 * tcrossprod(X, Y)
}


predict.my_knn_regressor = function(my_knn,x)
{
  print(x)
  if (!is.matrix(x))
  {
    x <- matrix(x, nrow=1, ncol = 2)
  }
  ## Compute pairwise distance
  dist_pair = compute_pairwise_distance(x,my_knn[['points']])
  print(dist_pair)
  ## orders the points by distance and select the k-closest points
  apply(dist_pair,1,order) <= my_knn[['k']], my_knn[["value"]]
  crossprod() / my_knn[['k']]
}