#!/usr/bin/env python
# coding: utf-8
1. __getattribute__ has a default implementation, but __getattr__ does not. This has a clear meaning: since __getattribute__ has a default implementation, while __getattr__ not, clearly python encourages users to implement __getattr__ .

2. The Cliff's Notes version: descriptors are a low-level mechanism that lets you hook into an object's attributes being accessed. Properties are a high-level application of this; that is, properties are implemented using descriptors

3. So, the difference between __getattribute__() and __getattr__() is that the first one is called unconditionally when an attribute is being retrieved from an instance while the second is called only when the attribute was not found.