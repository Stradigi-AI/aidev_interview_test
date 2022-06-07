
# AI Dev Interview Test
Build a Classification Pipeline that can train and predict via a RESTful API. The specific 
requirements and use cases that must be supported are listed below.


## Dataset information
The dataset has 10 feature columns, `V1`, `V2`, ..., `V10` and one target column,
called `Class`. The data type of the columns are:

- `V1`: numeric,
- `V2`: categorical with categories {Female,Male},
- `V3`: numeric,
- `V4`: numeric,
- `V5`: numeric,
- `V6`: numeric,
- `V7`: numeric,
- `V8`: numeric,
- `V9`: numeric,
- `V10`: numeric,
- `Class`: categorical with categories {1,2}.


## Use Cases
The rest api shall offer 2 endpoints: `train` and `predict`. Below are 
the 3 use cases that the api must support.  

<br />

#### Use Case 1: train on all features
The user can call the `train` endpoint with a single argument: the `id`
 of the model, as follows:

```commandline
Example
POST http://localhost:5000/{model_id}/train
Response Status: HTTP 201
Response Body: {"model_id": `model_id`}
```

This endpoint must train a model on the dataset `data/train.csv` in this repo. 
The `id` will be used to refer to the model in the `predict` command.  

<br />

#### Use Case 2: train with a subset of features
Optionally, the user may train a model on a subset of features. For example:

```commandline
Example
POST http://localhost:5000/{model_id}/train
Request Body: {"features": ["V1", "V2", "V3"]}
Response Status: HTTP 201
Response Body: {"model_id": `model_id`}
```

The semantic of the `train` endpoint is the following:

- First URL parameter: The `model_id`, will be used to refer to the model in the `predict` endpoint.
- POST JSON Body: A list of features to train on. 
  The request may contain other features that may or may not be in the dataset.
  Those extra features must be ignored.

This endpoint will train a model on the same dataset `data/train.csv`, but the 
model may only consider features provided in the optional `features` parameter 
(so `V1`, `V2` and `V3` in the above example). All the other features must 
be ignored. Any subset of features may be provided.

Note that the model `id` is still a mandatory argument and has the same meaning 
as in the first use case.

<br />

#### Use Case 3: predict on a dataset
The user may compute predictions specifying a model `id` 

```commandline
Example
POST http://localhost:5000/{model_id}/predict
Request Body: {"data": [{"V1": 46, "V2": "Female", "V3": 1.4, etc..}]}
Response Status: HTTP 200
Response Body: {"predictions": [1]}
```
The semantic of the `predict` endpoint is the following:

- First URL parameter: the `model_id`, it refers to the `id` of a model that was 
  previously trained using the `train` endpoint. 
- POST JSON Body: A list of features to make predictions on. 
  The request may contain other features that may or may not be in the dataset
  Those extra features must be ignored.
- POST Response: A list containing the prediction for each feature list

<br />

## Requirements

#### Functional Requirements
- The code should be extendable to other estimators (i.e. learning algorithms) in the future.
  To do so, a base class (an "interface") was provided in the `src/base.py` file. 
  Your learning algorithm is *required* to be a subclass of this base class.


#### Non-functional requirements:
- Must use Python 3.8, Pytest or Unittest
- Must not use any REST helper library. Ex: Flask-RESTful, Connexion
- Installation instructions must be provided. You may assume that the user of 
  the library has python 3.8 installed with the standard libraries available

___

### Evaluation
The code will be reviewed like any contribution to our code base. In particular,
software best practices should be followed (e.g. error handling, testing, etc.).



### Acceptance Tests
All the scripts in the `acceptance_tests` must run without errors until the end.



### How to Submit:
- Send a zip file containing all source code to your HR representative.
