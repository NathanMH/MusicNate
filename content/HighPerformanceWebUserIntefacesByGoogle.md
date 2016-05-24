Title:
Date:
Category:

Paul Lewis

- HTTPS
- Push Messaging
- Offline/Poor Connectivity

RAILs:
    - Response
    - Animation
    - Idle
    - Load

Side Navigation:
    - pointer-events: none;
      - Keep nav in render tree but won't block clicks
      - When nav is needed pointer-events: auto;
    - Promote to its own compositor layer
      - Don't do this to a lot of elements (uses a lot of memory)
    - will-change: transform;
    - transform: -102%;
    showSideNav (){
    	this.sideNavEl.classList.add('side-nav--visible');
    }

    .side-nav--visible .side-nav__container {
    	transform: none;
    }
