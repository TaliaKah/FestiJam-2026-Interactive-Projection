# FestiJam 2025 – Interactive Projection in a Geodesic Dome

An interactive audiovisual projection created for **FestiJam 2025**, presented inside a geodesic dome.

Visitors could interact with the projection using a tablet. The tablet interface allowed them to:

* choose different visual effects;
* select different brushes;
* draw directly on the tablet to interact with the projected visuals.

The projection was generated in real time using **Coollab**, with custom nodes developed for the project.

*The interactive projection during FestiJam 2025.*

## How it works

The installation consists of a computer running the visual system, a projector displaying the visuals inside the geodesic dome, and a tablet used as an interactive interface.

The tablet runs a local web interface. User interactions are sent to the visual system through **HTTP requests**, allowing visitors to modify the projection in real time.

The repository also contains an older **OSC-based communication system** (`server.py` and commented code in the web interface), which was used during development and is kept here for reference.

### Communication

```text
Tablet / Web interface
        │
        │ HTTP requests
        ▼
   Visual system
      (Coollab)
        │
        ▼
    Projector
```

## Project files

The repository contains the different parts of the installation:

* `Coollab Project/` — the Coollab project and visual system;
* `Web/` — the web interface used on the tablet, including its assets;
* `Server/` — Python code for the previous OSC-based communication system;
* `Coollab Project/Nodes/` — custom Coollab nodes used by the project;
* `Offline Resources/` — installers and other resources kept for offline installation.

### Custom Coollab node

This project uses a custom Coollab node.

Copy the contents of the `Coollab Project/Nodes/` folder to:

```text
C:\Users\[User Name]\AppData\Roaming\Coollab\Nodes
```

Then open the project with Coollab.

### Coollab version

This project requires **Coollab 1.6.1 – "Caching Experimental (FestiJam)"**.

This version can be selected through the Coollab launcher by enabling access to experimental versions and selecting the version above.

The project relies on a feature that is hardcoded in this experimental version of Coollab. As a result, the project **does not work correctly with other versions of Coollab**.

**Coollab version:** `1.6.1 – Caching Experimental (FestiJam)`

[Coollab](https://coollab-art.com/)

## Configuration

### HTTP communication

The IP address used by the web interface may need to be changed when running the project on another computer or network.

To find the computer's local IP address on Windows:

1. Open the Command Prompt.
2. Run:

   ```text
   ipconfig
   ```
3. Find the local IPv4 address of the computer.
4. Replace the old IP address in the web interface with the current one.

### OSC communication

If you want to use the older OSC-based communication system, the IP address in `Server/server.py` must also be updated.

The OSC-related code in the web interface is currently commented out.

## Offline resources

The `Offline Resources/` folder contains installers and other resources that were used to set up the installation at FestiJam 2025, where the project had to be installed and run without an Internet connection.

These files are kept in the repository so that the project can be installed on another computer without having to retrieve the required software again.

They are not normally required if the corresponding software is already installed on the system.

## Credits

**Project:** FestiJam 2025

**Created by:** Talia’Kah

**Tools:** Coollab, Node.js, Python, HTML/CSS/JavaScript

## License

Code and technical files may be freely inspected, modified and reused.

Artwork, visual effects and other original artistic content are not licensed for reuse.

See [LICENSE](LICENSE) for details.

## Note

This README was written with the assistance of AI. If you notice any errors or missing information, feel free to contact me.