#include <iostream>
#include <filesystem>
#include <string>

namespace fs = std::filesystem;

std::string findExternalDrive() {
  for (const auto& entry : fs::directory_iterator("/")) {
    if (fs::is_directory(entry) && fs::exists(entry) && !fs::is_empty(entry) && fs::is_empty(entry.path().root_directory())) {
      return entry.path().string();
    }
  }
  return "";
}

void copyFiles(const std::string& sourcePath, const std::string& destinationPath) {
  fs::copy(sourcePath, destinationPath, fs::copy_options::recursive | fs::copy_options::overwrite_existing);
}

int main() {
  std::string externalDrivePath = findExternalDrive();

  if (externalDrivePath.empty()) {
    std::cout << "No external drive found!" << std::endl;
    return 1;
  }

  std::cout << "Found external drive: " << externalDrivePath << std::endl;

  std::cout << "Enter the destination directory: ";
  std::string destinationPath;
  std::getline(std::cin, destinationPath);

  // Create the destination directory if it doesn't exist
  fs::create_directories(destinationPath);

  copyFiles(externalDrivePath, destinationPath);

  std::cout << "File transfer completed!" << std::endl;

  return 0;
}
