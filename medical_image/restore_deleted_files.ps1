# restore_deleted_files.ps1
param(
    [string]$CommitHash = "HEAD"
)

# Get all deleted files
$deletedFiles = git log --diff-filter=D --name-only --pretty=format: -- $CommitHash | Select-Object -Unique

Write-Host "Found $($deletedFiles.Count) deleted files" -ForegroundColor Yellow

foreach ($file in $deletedFiles) {
    if ($file -and $file.Trim()) {
        Write-Host "Restoring: $file" -ForegroundColor Green
        
        # Get the commit where it was deleted
        $commit = git log --diff-filter=D --pretty=format:"%H" -- $file | Select-Object -First 1
        
        if ($commit) {
            # Restore from the parent commit
            git checkout "$commit^" -- $file
        }
    }
}

Write-Host "Done!" -ForegroundColor Green