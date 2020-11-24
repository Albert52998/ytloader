import React from 'react';
import Header from "./Header";
import './main.css';
import './fonts/fonts.css';

export default function DownloadComplete() {
  return (
      <div>
        <Header />

        <div className="sign">
          <span className="sign__word">DOWNLOAD COMPLETE!</span>
        </div>
      </div>
  );
}