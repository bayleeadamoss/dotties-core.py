from behave import *
use_step_matcher("re")

# Given

@given(u'I have "(?P<package>[^"]*)" installed')
def step_impl(context, package):
    context.scenario.skip()

@given(u'"~/.zshrc" is no longer owned by my user')
def step_impl(context):
    context.scenario.skip()

@given(u'I have no files in "~/"')
def step_impl(context):
    context.scenario.skip()

@given(u'I have a file "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@given(u'I have a file "~/.zshrc" owned by root')
def step_impl(context):
    context.scenario.skip()

@given(u'I have a symlink "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@given(u'I have a dotties symlink "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@given(u'an old version of "(?P<package>[^"]*)" installed')
def step_impl(context, package):
    context.scenario.skip()

@given(u'I make a modification to "amjith/dotties"')
def step_impl(context):
    context.scenario.skip()

# When

@when(u'I type "(?P<command>[^"]*)"')
def step_impl(context, command):
    context.scenario.skip()

@when(u'I choose "y" to overwrite "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@when(u'I remove "blainesch/dotties" from the file system')
def step_impl(context):
    context.scenario.skip()

@when(u'I remove all the dotties in "~/"')
def step_impl(context):
    context.scenario.skip()

# Then

@then(u'I see the "(?P<screen>[^"]*)" screen')
def step_impl(context, screen):
    context.scenario.skip()

@then(u'I have no dotties in "~/"')
def step_impl(context):
    context.scenario.skip()

@then(u'I have no dotties directory in "~/"')
def step_impl(context):
    context.scenario.skip()

@then(u'I see my dotfiles installed')
def step_impl(context):
    context.scenario.skip()

@then(u'I am prompted asking if I want to overwrite "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@then(u'I see "Permission denied"')
def step_impl(context):
    context.scenario.skip()

@then(u'I see both packages installed')
def step_impl(context):
    context.scenario.skip()

@then(u'I see a list of files that would be installed')
def step_impl(context):
    context.scenario.skip()

@then(u'I see the new version of "(?P<package>[^"]*)"')
def step_impl(context, package):
    context.scenario.skip()

@then(u'I see the old version of "(?P<package>[^"]*)"')
def step_impl(context, package):
    context.scenario.skip()

@then(u'I see a prompt to telling us "amjith/dotties" is dirty')
def step_impl(context):
    context.scenario.skip()
