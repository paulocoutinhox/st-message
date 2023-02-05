# st-message

Streamlit Component, for a UI Message, Chat component

Authors - [@paulocoutinhox](https://github.com/paulocoutinhox) 

## Installation

Install this packages with PIP using:

```bash
python3 -m pip install git+https://github.com/paulocoutinhox/st-message
```

## Usage

Import the `message` function from `streamlit_message`

```python
import streamlit as st
from streamlit_message import message

message("My message") 
message("Hello World!", is_user=True)  # align's the message to the right
```
   
## Development

To install locally while develop use:

```bash
python3 -m pip install -e .
```