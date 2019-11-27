# ft_linear_regression
An Algo Project at Codam (42) - Linear Regression


## Project description

First of the projects in the machine learning area at 42 network. Objective is to create a linear regression function in the language of choise **(python3)**, train the model on the given dataset, save generated indexes and use them to predict car price depending on it's mileage. 

`ft_linear_regression.py` functions with `csv` files with `,` as separator

![Screenshots](/pic/regression.png)

## [SUBJECT](SUBJECT.ft_linear_regression.en.pdf)

## [Linear Regression - Wiki](https://en.wikipedia.org/wiki/Linear_regression)

## Usage

Clone and change directory to project, then
	
	python3 ft_linear_regression.py [path/to/dataset.csv [flags]]
	python3 predict.py your_desired_mileage

If no file is passed as a parameter, function asks to enter filename to standard input

### Flags

	-vs 	- visualize standardized dataset and solution
	-vo 	- visualize original dataset and solution
	-err 	- print mean squared error after each iteration of regression
	-lr 	- set learning rate (affects speed of learning), must be followed by a number
