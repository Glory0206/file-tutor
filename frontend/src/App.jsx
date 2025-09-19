import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Header } from "./features/chat/components/Header";
import { ChatPage } from "./pages/ChatPage";
import FileManagement from "./pages/FileManagement";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/chat" element={<ChatPage />} />
        <Route path="/files" element={<FileManagement />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
