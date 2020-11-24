import React from 'react';
import Header from "./Header";
import './main.css';
import './fonts/fonts.css';

export default function DownloadFailed() {
  return (
      <div>
        <Header />

        <div className="sign">
          <span className="sign__word">DOWNLOAD FAILED.</span>
        </div>
      </div>
  );
}