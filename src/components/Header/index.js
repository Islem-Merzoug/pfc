import React from 'react'

const Header = () => {
    return (
        <div>
            <div style={{height: "100%", width: "100%", display: "flex", overflow: "hidden"}}>
                <img src={'/images/—Pngtree—robot artificial intelligence robot blue_926814.jpg'} alt='Home Page'/>

                <div style={{ color: '#fff', position: 'absolute', top: "30%", left: "40%", transform: "translate(-90%, -10%)" }}>
                    <div style={{ fontSize: '15px' }} >
                        <div>
                            IMED Bejaia MODEL GALLERY
                        </div>
                        <div>
                            Discover open source deep learning code and pretrained models.
                        </div>
                    </div>

                    <div style={{ fontSize: '35px', paddingTop: '10px', fontWeight: 'bolder'}} >
                        <div>
                            Pre- trained AI Models
                        </div>
                        <div>
                            to get you started 
                        </div>
                    </div>

                    <div style={{ fontSize: '24px', paddingTop: '10px', fontStyle: 'italic'}}>
                        <div>
                            Explore the IMED club pre-build,
                        </div>
                        <div>
                            ready-to-use AI models to suit your specific use cases
                        </div>
                    </div>

                </div>               
            </div>
        </div>
    )
}

export default Header
