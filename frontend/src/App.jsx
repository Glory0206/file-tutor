import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Header } from "./features/chat/components/Header";
import { ChatPage } from "./pages/ChatPage";
import FileManagement from "./pages/FileManagement";

function App() {
  return (
    <BrowserRouter>
      <div
        style={{ display: "flex", flexDirection: "column", height: "100vh" }}
      >
        <Header />
        <main style={{ flex: 1, overflowY: "auto" }}>
          <Routes>
            <Route path="/chat/:fileId" element={<ChatPage />} />
            <Route path="/chat" element={<ChatPage />} />
            <Route path="/files" element={<FileManagement />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
