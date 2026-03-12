/ [Home](index.md)

## Kiro Spec



### Steering - always.md
```
---
inclusion: always
---

# General Rules

## Custom
- don't hardcode anything as a fallback when you get exception. It's dangerous and misleading
- when I say reqs or REQS, I mean requirements.txt
- if you see file name called .ant, consider it is my custom "admin notes" file where I keep some notes for admin purposes. It is not related to anything in Java. It's pure local custom notes.
- when you deal with prompts in python, keep the prompts separated in "prompts/*.txt". It should not be attached with python code. It should be always in .txt file.


## Random Data Maker
- When you are asked to use random city or such things, use "randum" python library from https://pypi.org/project/randum/1.0.9/. Also, refer the documentation of `randum` library here: https://deepwiki.com/kactlabs/randum.

## Documentation
- Never add any new .md/.txt file for documenting anything.
- If any documention, update README.md

## Acronym
- SS - Screenshots; when I type SS, assume I am talking about screenshots
- reqs/REQs/REQS - requirements.txt
```


### Steering - ui-guidelines.md
```
---
inclusion: manual
---

# General Rules

## Documentation

Never add any new .md file for documenting anything.

# UI Guidelines

## Modal vs Alert

When a page has any popup option, use modal instead of `js-alert` (JavaScript alert dialogs).

**Why:** Modals provide better UX with custom styling, accessibility, and control over the interaction flow.

## Notifications

For notifications and user feedback, use a top-right toaster component instead of alerts.

**Implementation:**
- Display toaster notifications in the top-right corner of the viewport
- Use appropriate toast types: success, error, warning, info
- Auto-dismiss after appropriate duration (typically 3-5 seconds)
- Allow manual dismissal via close button
```