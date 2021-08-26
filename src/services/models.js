export const models = [
    {
        id: 0,
        name: 'Skin Segmentation',
        image: "/images/—Pngtree—robot artificial intelligence robot blue_926814.jpg",
        description: 'Beginning with a color image, the first stage is to transform it to a skin-likelihood image. This involves transforming every pixel from RGB representation to chroma representation and determining the likelihood value based on the equation given in the previous section. The skin-likelihood image will be a gray-scale image whose gray values represent the likelihood of the pixel belonging to skin. A sample color image and its resulting skin-likelihood image are shown in Figure 3. All skin regions (like the face, the hands and the arms) were shown brighter than the non-skin region.',
        detailLink: '/modelDetails/0',
        inputImageExempleLink: '/images/ex_skinseg_input.jpeg',
        outputImageExempleLink: '/images/ex_skinseg_output.jpeg',
        executeLink: 'http://localhost:8000/predict_skinseg',
        exportLink: 'http://localhost:8000/export_skinseg'
        
    },
    {
        id: 1,
        name: 'Object Detection',
        image: "/images/nfcread-yuz-tanima-face-matching.jpeg",
        description: "En vision par ordinateur on désigne par détection d'objet une méthode permettant de détecter la présence d'une instance ou d'une classe d'objets dans une image numérique. Une attention particulière est portée à la détection de visage et la détection de personne.",
        detailLink: '/modelDetails/1',
        inputImageExempleLink: '/images/ex_yolo_output.jpeg',
        outputImageExempleLink: '/images/ex_yolo_output.jpeg',
        executeLink: 'http://localhost:8000/predict_yolov',
        exportLink: 'http://localhost:8000/export_yolov'
        
    }
]

