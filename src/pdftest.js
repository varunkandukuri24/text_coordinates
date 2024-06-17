import React from 'react';
import { PDFDocument, StandardFonts, rgb } from 'pdf-lib';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Get the directory name from the URL of the current module
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const pdftest = async () => {
    const formPdfPath = path.join(__dirname, './assets/b2form.pdf');
    const formPdfBytes = fs.readFileSync(formPdfPath);
    const pdfDoc = await PDFDocument.load(formPdfBytes, { ignoreEncryption: true });

    console.log(pdfDoc);
}

export default pdftest

pdftest();