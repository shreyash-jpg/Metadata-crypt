## Metadata-crypt
#🔐 MetaCrypt – CLI-Based Metadata Protection Tool
MetaCrypt is a command-line based Python tool designed to secure and protect metadata in files such as images, documents, and multimedia.  
Instead of simply removing metadata, MetaCrypt offers multiple protection modes — encryption, obfuscation, sanitization, and restoration — ensuring your privacy while keeping files functional.                                 

#📜 Introduction
Every file we create or share contains metadata — hidden information that may include creation dates, author names, device IDs, software versions, and even GPS coordinates.  
While metadata is useful for organization and file tracking, it can also expose sensitive information to hackers, forensic analysts, or malicious third parties.
Simply deleting metadata is not always the best approach, as it may:
Cause compatibility issues.
Remove valuable context for legitimate use.
Raise suspicion in forensic or compliance environments.
MetaCrypt solves this by allowing users to:
Encrypt metadata with strong cryptography.
Obfuscate values with random or fake data.
Sanitize files by stripping all unnecessary metadata.
Restore encrypted metadata with the correct decryption key.
MetaCrypt is lightweight, cross-platform, and designed for cybersecurity professionals, privacy advocates, journalists, and organizations handling sensitive digital content.                   

#🎯 Objectives  
Provide a lightweight, portable, CLI-based metadata security tool.  
Support encryption, obfuscation, and sanitization of metadata.   
Maintain file usability and integrity after modification.   
Support restoring metadata with a valid decryption key.                 

#📌 Scope  
Supported File Types   
Images: `.jpg`, `.jpeg`, `.png`, `.webp`  
Documents: `.pdf`, `.docx`   
Multimedia (limited): `.mp3`, `.mp4`   
Features   
Command	Description   
`--scan`	Display current metadata  
`--encrypt`	Encrypt metadata values   
`--obfuscate`	Replace metadata with fake/random values  
`--sanitize`	Remove metadata entirely  
`--restore`	Restore encrypted metadata (requires key)   

#🖥️ Hardware Requirements  
    Component	Minimum Requirement  
    Processor	Dual-core 2.0 GHz or higher  
    RAM	2 GB (4 GB recommended)  
    Storage	200 MB free space  
    Display	CLI-compatible terminal  

#💻 Software Requirements  
     Component	Specification   
     OS	Windows 10+, Linux (Ubuntu 20.04+), macOS   
     Python Version	Python 3.8+   
     Required Libraries	`cryptography`, `Pillow`, `PyPDF2`, `python-docx`, `piexif`, `Faker`, `argparse`  
     Optional Tool	`exiftool` for deeper metadata access   
#Install dependencies:   
  bash  
   pip install cryptography Pillow PyPDF2 python-docx piexif Faker argparse
     

#⚙️ Installation   
   Clone the Repository  
   ```bash  
      git clone https://github.com/yourusername/metacrypt.git
     cd metacrypt
   ```
Install Required Python Packages  
   ```bash
     pip install -r requirements.txt
   ```
Run the Tool   
    ```bash
    python metacrypt.py --help  
     ```

#🚀 Usage 
  Scan Metadata
   ```bash
    python metacrypt.py --file sample.jpg --scan
   ```
  Encrypt Metadata 
   ```bash
     python metacrypt.py --file sample.jpg --encrypt --key my.key
   ```
  Obfuscate Metadata  
   ```bash    
    python metacrypt.py --file sample.pdf --obfuscate  
  ```  
  Sanitize (Remove All Metadata)  
   ```bash  
     python metacrypt.py --file confidential.docx --sanitize  
   ```   
  Restore Encrypted Metadata   
   ```bash  
    python metacrypt.py --file sample.jpg --restore --key my.key
   ```  

#🔒 Security Notes    
Always store your encryption key securely. Losing it means you cannot restore original metadata.  
MetaCrypt does not modify the content of files — only their metadata.  
The tool is intended for ethical and privacy-focused use only.   
