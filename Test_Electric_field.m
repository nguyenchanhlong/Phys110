function Electric_field_vector_Particles
% Author: Tran Hai Cat
% Lecturer in Physics, HCM University of Technology and Education
% - Dai hoc Su pham Ky thuat Tp. Ho Chi Minh
% Created: 2019.02.01
clc;
clear all;
close all;
%% INPUT DATA
ke = 9e9;
Q = [1]*1e-9; % charges

xQ = [0]; % coordinates of charges
yQ = [0];
zQ = [0];

xA = 1;
yA = 1;
zA = 1;
% 
r = sqrt((xA-xQ)^2+(yA-yQ)^2+(zA-zQ)^2);
 
 rx = (xA-xQ)/r;
 ry = (yA-yQ)/r;
 rz = (zA-zQ)/r;
 
 E0 = ke*Q/r^2;
 
 Ex = E0*rx
 Ey = E0*ry
 Ez = E0*rz

streak_arrow = 1; % 1-MUI TEN CONG, 0-MUI TEN THANG

xmin = -1; xmax = 1; ymin = -1; ymax = 1; zmin = -1; zmax = 1;
%% CALCULATION
N = length(Q);
Nx = 10;
Ny = 10;
Nz = 10;
x = linspace(xmin,xmax,Nx);
y = linspace(ymin,ymax,Ny);
z = linspace(zmin,zmax,Nz);
[X,Y,Z] = meshgrid(x,y,z);

ke = 9e9;
Ex = zeros(size(X));
Ey = zeros(size(Y));
Ez = zeros(size(Z));


for iN = 1:N
r = sqrt((X-xQ(iN)).^2+(Y-yQ(iN)).^2+(Z-zQ(iN)).^2);
E = ke*Q(iN)./r./r;

Ex = Ex+E./r.*(X-xQ(iN)); % x-component of vector field
Ey = Ey+E./r.*(Y-yQ(iN)); % y-component of vector field
Ez = Ez+E./r.*(Z-zQ(iN)); % z-component of vector field

condition = find(r<0.3);
Ex(condition) = 0;
Ey(condition) = 0;
Ez(condition) = 0;
end

%% FIGURES
figure('name','Electric Field Vector 3D','color','w','numbertitle','off');
if streak_arrow
streakarrow3d(X,Y,Z,Ex,Ey,Ez,2,1);
else
quiver3(X,Y,Z,Ex,Ey,Ez,'AutoScaleFactor',3);
end
hold on

% Draw charged particles:
for iN = 1:N
[x1, y1, z1] = sphere(24);
radius = 0.1;
x1 = x1(:)*radius+xQ(iN);
y1 = y1(:)*radius+yQ(iN);
z1 = z1(:)*radius+zQ(iN);
P = [x1 y1 z1];
P = unique(P,'rows');

shp = alphaShape(P,1.5);
plot(shp)
end

%% Axis properties
axis equal
axis([xmin xmax ymin ymax zmin zmax]);
rotate3d on

xlabel('X, m');
ylabel('Y, m');
zlabel('Z, m');
view(-20,30);
box on
grid off
set(gca,'color','w')

function hh=streakarrow3d(X,Y,Z,U,V,W,np,AC)
%% Bertrand Dano 03-09
% Copyright 1984-2009 The MathWorks, Inc.
DX=abs(X(1,1,1)-X(1,2,1)); DY=abs(Y(1,1,1)-Y(2,1,1)); DZ=abs(Z(1,1,1)-Z(1,1,2));
DD=min([DX DY DZ]);
ks=DD/100; % Size of the "dot" for the tuft graphs
np=np*10;
alpha = 3; % Size of arrow head relative to the length of the vector
beta = .15; % Width of the base of the arrow head relative to the length
XYZ=stream3(X,Y,Z,U,V,W,X,Y,Z);
Vmag=sqrt(U.^2+V.^2+W.^2);
Vmin=min(Vmag(:));Vmax=max(Vmag(:));
Vmag=Vmag(:);
cmap=colormap;
for k=1:length(XYZ)
F=XYZ(k); [L M]=size(F{1});
if L<np
F0{1}=F{1}(1:L,:);
if L==1
F1{1}=F{1}(L,:);
else
F1{1}=F{1}(L-1:L,:);
end

else
F0{1}=F{1}(1:np,:);
F1{1}=F{1}(np-1:np,:);
end
P=F1{1};
if AC==1
vcol=floor((Vmag(k)-Vmin)./(Vmax-Vmin)*64); if vcol==0; vcol=1; end
COL=[cmap(vcol,1) cmap(vcol,2) cmap(vcol,3)];
else
COL='k';
end
hh=streamline(F0);
set(hh,'color',COL,'linewidth',.5);

if L>1
x1=P(1,1); y1=P(1,2); z1=P(1,3);
x2=P(2,1); y2=P(2,2); z2=P(2,3);
u=x2-x1; v=y2-y1; w=z2-z1; uv=sqrt(u.*u + v.*v);

xa1=x2+u-alpha*(u+beta*(v+eps)); xa2=x2+u-alpha*(u-beta*(v+eps)); xa3=x2+u-alpha*u;
ya1=y2+v-alpha*(v-beta.*(u+eps)); ya2=y2+v-alpha*(v+beta.*(u+eps)); ya3=y2+v-alpha*v;
za1=z2+w-alpha*w; za2=z2+w-alpha*(w+beta.*(uv+eps)); za3=z2+w-alpha*(w-beta.*(uv+eps));

plot3([x2 xa1 xa2 x2 xa3 xa3 x2],[y2 ya1 ya2 y2 ya3 ya3 y2],[z2 za1 za1 z2 za2 za3 z2],'color',COL); hold on
end

end
axis image