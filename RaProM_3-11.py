#!/usr/bin/env python
"""Backward-compatible CLI wrapper for raprom.

The processing module has been renamed to `raprom` so it can be imported
from notebooks (`import raprom`). This shim preserves the documented
`python RaProM_3-11.py PATH ...` invocation.
"""
from raprom import main

if __name__ == '__main__':
    main()
