---
name: Custom issue template
about: Describe this issue template's purpose here.
title: Bug
labels: ''
assignees: koagonzalo11

---

name: Custom Issue Template
description: Describe this issue template's purpose here.
title: "[ISSUE] "  # Default title prefix
labels: []  # Add default labels if needed
assignees: []  # Assign users if needed
body:
  - type: markdown
    attributes:
      value: |
        ## ⚡ Custom Issue Template  
        Please fill in the details below to help us understand the issue better.  

  - type: textarea
    id: issue_description
    attributes:
      label: "🔍 Issue Description"
      description: "Describe the issue or feature request in detail."
      placeholder: "Provide a clear and concise description..."
    validations:
      required: true

  - type: textarea
    id: expected_behavior
    attributes:
      label: "✅ Expected Behavior"
      description: "What should happen instead?"
      placeholder: "Describe the expected outcome..."
    validations:
      required: false

  - type: textarea
    id: actual_behavior
    attributes:
      label: "⚠️ Actual Behavior"
      description: "What actually happens?"
      placeholder: "Describe what you observed..."
    validations:
      required: false

  - type: dropdown
    id: environment
    attributes:
      label: "🖥️ Environment"
      description: "Where did this issue occur?"
      options:
        - "Production"
        - "Staging"
        - "Local Development"
        - "Other"
    validations:
      required: false

  - type: input
    id: additional_info
    attributes:
      label: "📌 Additional Info"
      description: "Any other relevant details (logs, screenshots, etc.)?"
      placeholder: "Paste links or notes here..."
    validations:
      required: false
