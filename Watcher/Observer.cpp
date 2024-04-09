#include <iostream>
#include <fstream>
#include <Windows.h>
#include <string>
#include <thread>
#include <filesystem>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <cstdlib>

namespace fs = std::filesystem;
using namespace std;

queue<wstring> messageQueue;  
mutex mtx;                    
condition_variable cv;       


void createCache() {
    fs::path temp_dir = fs::temp_directory_path();
    fs::path file_path = temp_dir / "WatcherCache.txt";

    if (fs::exists(file_path)) {
        std::cout << "Cache file already exists: " << file_path << std::endl;
        return;
    }

    std::ofstream file(file_path);

    if (!file.is_open()) {
        std::cerr << "Error opening file for writing: " << file_path << std::endl;
        return;
    }

   
    file << "D:\\Games\\TEST" << std::endl;
    std::cout << "Cache file created successfully: " << file_path << std::endl;
}

static void ReadCache()
{
    while (true)
    {   
        filesystem::path temp_dir = std::filesystem::temp_directory_path();
        filesystem::path file_path = temp_dir / "WatcherCache.txt";

        ifstream inFile(file_path);

        if (!inFile.is_open()) {
            cout << "Error opening file" << endl;
        }

        string line;
        while (getline(inFile, line)) {
            wstring wideString(line.begin(), line.end());

            // Lock the mutex before pushing to the queue
            unique_lock<mutex> lock(mtx);
            messageQueue.push(wideString);
            lock.unlock();  // Unlock the mutex

            // Notify waiting threads that new message is available
            cv.notify_all();
        }

        // Wait for 1 second before starting the loop again
        this_thread::sleep_for(chrono::seconds(1));
    }
}
static void Watcher()
{
    while (true)
    {
        // Lock the mutex before accessing the queue
        unique_lock<mutex> lock(mtx);

        if (!messageQueue.empty()) {
            wstring message = messageQueue.front();
            messageQueue.pop();
            lock.unlock();

            LPCWSTR wideStringPtr = message.c_str();
            wcout << wideStringPtr << endl;
            HANDLE hchange = FindFirstChangeNotificationW(wideStringPtr, FALSE, FILE_NOTIFY_CHANGE_FILE_NAME);
            DWORD dwWaitStatus = WaitForSingleObject(hchange, 1000);

            if (dwWaitStatus == WAIT_OBJECT_0)
            {
                cout << "Chage Deteched....";
                int systems = system("python \"C:/Users/somkr/OneDrive/Desktop/Data Structures/test.py\"");
            }
        }
    }
}

  
int main()
{
    createCache();
    thread Worker_1(ReadCache);
    thread Worker_2(Watcher);

    Worker_1.join();
    Worker_2.join();

    return 0;
}
