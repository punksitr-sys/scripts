# scripts
⚠️ Tip: Review script content before `chmod +x`  
<br>

## fk.sh
`fk.sh` is a bash wrapper for `faketime`. Accept hour offset, run command with spoofed system time.

Get UTC time:
- Linux `date -u` 
- Windows `[System.DateTime]::UtcNow`

Create symlink for global command: `sudo ln -s /usr/local/scripts/fk.sh /usr/local/bin/fk`  
Usage: `fk <offset_hours> <command...>`  
Example: `fk +2 whoami`

<br>

## get_ports.py
Extract open TCP/UDP port numbers from Nmap plaintext output.  
- Default delimiter: `,`  
- Support escaped delimiters like `\n`, `\t`  

Create symlink for global command: `sudo ln -s /usr/local/scripts/get_ports.py /usr/local/bin/getports`  
Usage: `getports <nmap_output_file> [delimiter]`  
Example: `getports nmap.txt`  
