# Install Azure CLI


Download and install the latest release of the Azure CLI. When the installer asks if it can make changes to your computer, click the "Yes" box. [Link](https://aka.ms/installazurecliwindows)


You can now run the Azure CLI with the az command from either Windows Command Prompt or PowerShell.

## Enable Tab Completion on PowerShell

PowerShell provides completion on inputs to provide hints, enable discovery and speed up input entry. Command names, command group names, parameters and certain parameter values can be completed by pressing the Tab key

To enable tab completion in PowerShell, create or edit the profile stored in the variable `$PROFILE`. The simplest way is to run notepad `$PROFILE` in PowerShell.

Then add the following code to your PowerShell profile:

```powershell
Register-ArgumentCompleter -Native -CommandName az -ScriptBlock {
    param($commandName, $wordToComplete, $cursorPosition)
    $completion_file = New-TemporaryFile
    $env:ARGCOMPLETE_USE_TEMPFILES = 1
    $env:_ARGCOMPLETE_STDOUT_FILENAME = $completion_file
    $env:COMP_LINE = $wordToComplete
    $env:COMP_POINT = $cursorPosition
    $env:_ARGCOMPLETE = 1
    $env:_ARGCOMPLETE_SUPPRESS_SPACE = 0
    $env:_ARGCOMPLETE_IFS = "`n"
    az 2>&1 | Out-Null
    Get-Content $completion_file | Sort-Object | ForEach-Object {
        [System.Management.Automation.CompletionResult]::new($_, $_, "ParameterValue", $_)
    }
    Remove-Item $completion_file, Env:\_ARGCOMPLETE_STDOUT_FILENAME, Env:\ARGCOMPLETE_USE_TEMPFILES, Env:\COMP_LINE, Env:\COMP_POINT, Env:\_ARGCOMPLETE, Env:\_ARGCOMPLETE_SUPPRESS_SPACE, Env:\_ARGCOMPLETE_IFS
}
```

To display all available options in the menu, add `Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete`  to your PowerShell profile.

## How to sign into the Azure CLI

We can run azure cli from our bash or we can use cloud shell from azure which is currently connected.

```powershell
az login
```

If the CLI can open your default browser, it will initiate authorization code flow and open the default browser to load an Azure sign-in page.



# Deploy in Azure




1. Create a Resource Group
2. Create a Virtual Network and a subnet
3. Protect a subnet using a Network Security Group
4. Deploy Bastion to connect to a Virtual Machine
5. Create an Ubuntu Server Virtual Machine
6. Install Nextcloud by connecting via SSH using Bastion
7. Publish an IP
8. Create a DNS label