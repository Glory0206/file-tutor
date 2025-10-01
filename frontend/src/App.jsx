import { BrowserRouter, Routes, Route, Outlet } from "react-router-dom";
import { Header } from "./features/components/Header";
import { ChatPage } from "./pages/ChatPage";
import FileManagement from "./pages/FileManagement";
import LoginPage from "./pages/LoginPage";

const MainLayout = () => (
  <div style={{ display: "flex", flexDirection: "column", height: "100vh" }}>
    <Header />
    <main style={{ flex: 1, overflowY: "auto" }}>
      <Outlet />
    </main>
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/login" element={<LoginPage />} />

        <Route element={<MainLayout />}>
          <Route path="/chat/:fileId" element={<ChatPage />} />
          <Route path="/chat" element={<ChatPage />} />
          <Route path="/files" element={<FileManagement />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
