# Puppet manifest to modify a specific line in a file on a server

# Define the path to the file that needs editing
$file_to_edit = '/var/www/html/wp-settings.php'

# Use the 'exec' resource to execute a command for replacing text in the file
# The command below uses 'sed' to search for the string "phpp" and replace it with "php"
# The '-i' option edits the file in-place
exec { 'replace_line_in_file':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  # Define the directories where the 'sed' command can be found
  path    => ['/bin', '/usr/bin']
}
