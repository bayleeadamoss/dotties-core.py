from behave import *

@when(u'I type "dotties"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the "help" screen')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "sudo dotties"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the "sudo of shame" screen')
def step_impl(context):
    context.scenario.skip()

@given(u'I have "blainesch/dotties" installed')
def step_impl(context):
    context.scenario.skip()

@given(u'"~/.zshrc" is no longer owned by my user')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties doctor"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the "take ownership" screen')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties help"')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties help install"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the "install help" screen')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties implode"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should have no dotties in "~/"')
def step_impl(context):
    context.scenario.skip()

@then(u'I have no dotties directory in "~/"')
def step_impl(context):
    context.scenario.skip()

@given(u'I have no files in "~/"')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties install blainesch/dotties"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see my dotfiles installed')
def step_impl(context):
    context.scenario.skip()

@given(u'I have a file "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should be prompted asking if I want to overwrite "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@given(u'I have a file "~/.zshrc" owned by root')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "y" to overwrite "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see "Permission denied"')
def step_impl(context):
    context.scenario.skip()

@given(u'I have a symlink "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@given(u'I have a dotties symlink "~/.zshrc"')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties install amjith/dotties"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see both packages installed')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties install --dry blainesch/dotties"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see a list of files that would be installed')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties install tinytacoteam/does_-not_exist"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the "repo of shame" screen')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties uninstall blainesch/dotties"')
def step_impl(context):
    context.scenario.skip()

@when(u'I remove "blainesch/dotties" from the file system')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties update"')
def step_impl(context):
    context.scenario.skip()

@when(u'I remove all the dotties in "~/"')
def step_impl(context):
    context.scenario.skip()

@given(u'an old version of "blainesch/dotties" installed')
def step_impl(context):
    context.scenario.skip()

@given(u'an old version of "amjith/dotties" installed')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the new version of "blainesch/dotties"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the new version of "amjith/dotties"')
def step_impl(context):
    context.scenario.skip()

@given(u'I make a modification to "amjith/dotties"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see a prompt to telling us "amjith/dotties" is dirty')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the old version of "amjith/dotties"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the old version of "blainesch/dotties"')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties update blainesch/dotties"')
def step_impl(context):
    context.scenario.skip()

@given(u'I have an old version of "blainesch/dotties" installed')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties update --dry blainesch/dotties"')
def step_impl(context):
    context.scenario.skip()

@when(u'I type "dotties version"')
def step_impl(context):
    context.scenario.skip()

@then(u'I should see the "version" screen')
def step_impl(context):
    context.scenario.skip()
