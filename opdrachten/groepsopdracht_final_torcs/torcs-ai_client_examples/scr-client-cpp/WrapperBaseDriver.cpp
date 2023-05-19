/***************************************************************************
 
    file                 : WrapperBaseDriver.cpp
    copyright            : (C) 2007 Daniele Loiacono
 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
#include "WrapperBaseDriver.h"

void writeCsvRow(CarState X, CarControl Y) {
	/**
     * CSV Representation
    */
    // X : Data from Server
    
    // 8 Car State Features
    printf("%f;%f;%f;%i;%i;%f;%f;%f", X.getSpeedX(), X.getSpeedY(), X.getSpeedZ(), X.getRpm(), X.getGear(),  X.getAngle(), X.getZ(), X.getDamage());
    printf(";");

    // 6 Race Environment Features
    printf( "%f;%i;%f;%f;%f;%f", X.getTrackPos(), X.getRacePos(), X.getDistRaced(), X.getDistFromStart(), X.getCurLapTime(), X.getLastLapTime());
    printf(";");

    // Y : Data from Agent
    // 5 Actions
    printf("%f;%f;%i;%f;%f", Y.getAccel(), Y.getBrake(), Y.getGear(), Y.getSteer(), Y.getClutch());
    printf("\n");

}

string 
WrapperBaseDriver::drive(string sensors)
{
	CarState cs(sensors);
	CarControl cc = wDrive(cs);
    writeCsvRow(cs, cc);
	return cc.toString();	
}

