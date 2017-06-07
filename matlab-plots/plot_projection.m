% Plots the 3D convex polyhedron and the projected point

load('plot_data.mat');
faces = faces + 1;     % Correct indexing
point = double(point);

% Get matlab default colors
matlab_colors = get(groot, 'DefaultAxesColorOrder');

% Setup the figure
figure;
hold on;
axis equal;

% Plot the polyhedron
trisurf(faces, vertices(:, 1), vertices(:, 2), vertices(:, 3), 'EdgeColor', [1, 1, 1], 'FaceColor', matlab_colors(1, :), 'EdgeAlpha', 0.3, 'FaceAlpha', 0.3);

% Plot the projection of the point on the polyhedron
pp = [point; projected_point];
plot3(pp(:, 1), pp(:, 2), pp(:, 3), 'linewidth', 2, 'color', matlab_colors(2, :), 'marker', 'x');
