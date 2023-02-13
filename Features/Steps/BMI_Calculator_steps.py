from behave import *

# The step file contains the implementation of the steps that we have described in the feature file.

@given('I enter the "{Age}"')
def step_impl(context, Age):
    context.bmipage.age_input(Age)


@when('I Click on "{Gender}"')
def step_impl(context, Gender):
    context.bmipage.gender_radio(Gender)

@step('I Enter a "{height}"')
def step_impl(context, height):
    context.bmipage.height_input(height)

@step('I Enter the "{weight}"')
def step_impl(context, weight):
    context.bmipage.weight_input(weight)

@step("I Click on Calculate btn")
def step_impl(context):
    context.bmipage.calculatebtn_click()

@step('I Verify Result with "{expresult}"')
def step_impl(context, expresult):
    context.bmipage.result_validation(expresult)