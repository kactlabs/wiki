/ [Home](index.md)

## Oh My Posh


### Windows

### 1. Install PowerShell 7
```powershell
winget install Microsoft.PowerShell
```

### 2. Install Oh My Posh
```powershell
winget install JanDeLaHaye.OhMyPosh
```

### 3. Install a Nerd Font
Download **MesloLGS NF** or **CaskaydiaCove NF** from [nerdfonts.com](https://www.nerdfonts.com/font-downloads)

- Install the font
- Open Windows Terminal → Settings → Profiles → PowerShell
- Set **Font face** to your chosen Nerd Font

### 4. Set the Color Scheme

In **Windows Terminal → Settings → Open JSON file**, add to `"schemes"`:
```json
{
  "name": "MaroonDark",
  "background": "#2D0A1E",
  "foreground": "#E0D0D8",
  "black": "#1A0010",
  "red": "#FF5555",
  "green": "#50FA7B",
  "yellow": "#F1FA8C",
  "blue": "#6272A4",
  "purple": "#BD93F9",
  "cyan": "#8BE9FD",
  "white": "#F8F8F2",
  "brightBlack": "#44475A",
  "brightRed": "#FF6E6E",
  "brightGreen": "#69FF94",
  "brightYellow": "#FFFFA5",
  "brightBlue": "#D6ACFF",
  "brightPurple": "#FF92DF",
  "brightCyan": "#A4FFFF",
  "brightWhite": "#FFFFFF"
}
```

Then in your PowerShell profile entry, set:
```json
"colorScheme": "MaroonDark"
```

### 5. Apply an Oh My Posh Theme

Open your PowerShell profile:
```powershell
notepad $PROFILE
```

Add this line:
```powershell
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\jandedobbeleer.omp.json" | Invoke-Expression
```

> Run `Get-PoshThemes` to preview all available themes and find the closest match.

### 6. Reload Profile
```powershell
. $PROFILE
```

---

### Prompt Segments Reference

| Segment | Color | Description |
|--------|-------|-------------|
| `pwsh` | Cyan pill | Shell indicator |
| Folder icon | Orange | Current directory |
| `7ms` | Teal | Command execution time |
| Windows icon | Blue | OS indicator (right side) |
| `88%` | Yellow/Green | Battery level (right side) |
| `5, 11:15` | Blue | Date and time (right side) |

---

### Tips

- Right-side segments (OS, battery, clock) are built into themes like `jandedobbeleer`
- To customize segments, copy the theme JSON and edit it:
```powershell
cp "$env:POSH_THEMES_PATH\jandedobbeleer.omp.json" "$HOME\my-theme.omp.json"
notepad "$HOME\my-theme.omp.json"
```

- Then point your profile to your custom theme:
```powershell
oh-my-posh init pwsh --config "$HOME\my-theme.omp.json" | Invoke-Expression
```